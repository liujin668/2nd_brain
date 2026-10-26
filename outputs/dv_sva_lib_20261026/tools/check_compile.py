#!/usr/bin/env python3
"""Parse, type-check and elaborate the library. This does NOT simulate SVA."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MATRIX = r'''`include "dv_sva_macros.svh"
module dv_sva_compile_matrix;
  timeunit 1ns; timeprecision 1ps;
  logic clk, rst_n, other_clk, other_rst_n, a, b;
  logic [1:0] vector;
  `DV_SVA_ASSERT(a_generic, a |=> b)
  `DV_SVA_ASSERT_MSG(a_message, a |-> b, "custom message")
  `DV_SVA_ASSERT(a_other_clock, a |=> b, other_clk, other_rst_n)
  `DV_SVA_KNOWN(a_concat_known, ({a, b}))
  `DV_SVA_HOLD_WHEN_STALLED(a_hold, a, b, vector)
  always_comb begin
    `DV_SVA_ASSERT_IMMEDIATE(a_immediate, !$isunknown(a))
  end
  dv_sva_response_window #(.MIN_CYCLES(0), .MAX_CYCLES(0), .TRIGGER_ON_RISE(0))
    u_zero_window (.clk(clk), .rst_n(rst_n), .req_i(a), .rsp_i(b));
  dv_sva_ready_valid #(.DATA_WIDTH(1), .CHECK_PAYLOAD_KNOWN(0))
    u_one_bit (.clk(clk), .rst_n(rst_n), .valid_i(a), .ready_i(b), .data_i(a));
  dv_sva_fifo #(.DEPTH(1), .ALLOW_FULL_REPLACE(0), .ALLOW_EMPTY_BYPASS(0))
    u_no_replace (.clk(clk), .rst_n(rst_n), .push_i(a), .pop_i(b),
      .full_i(a), .empty_i(b), .count_i(a));
endmodule
'''
UVM_STUB = r'''// Compile-only signature stub; NOT the UVM library or a runtime test.
package uvm_pkg;
  timeunit 1ns; timeprecision 1ps;
  parameter int UVM_NONE = 0;
  function automatic void uvm_report_error(string id, string message,
      int verbosity=0, string filename="", int line=0);
  endfunction
endpackage
'''


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pyslang-path', type=Path, help='Optional pip --target directory')
    parser.add_argument('--stage-root', type=Path, help='Optional parent for a compiler staging directory')
    args = parser.parse_args()
    if args.pyslang_path:
        sys.path.insert(0, str(args.pyslang_path.resolve()))
    try:
        import pyslang
        from pyslang.ast import Compilation
        from pyslang.syntax import SyntaxTree
        from pyslang.parsing import PreprocessorOptions
    except ImportError:
        print('Install optional compiler: python -m pip install -r tools/requirements-static.txt', file=sys.stderr)
        return 2
    sources = sorted(ROOT.glob('checkers/*.sv')) + sorted(ROOT.glob('examples/*.sv')) + sorted(ROOT.glob('tests/*.sv'))
    results = []
    parent = (args.stage_root or Path(tempfile.gettempdir())).resolve()
    parent.mkdir(parents=True, exist_ok=True)
    original_cwd = Path.cwd()
    # Fresh isolated copy also avoids native Windows Unicode-path limitations.
    with tempfile.TemporaryDirectory(prefix='dv-sva-compile-', dir=parent) as directory:
        stage = Path(directory).resolve()
        if stage.parent != parent or not stage.name.startswith('dv-sva-compile-'):
            raise RuntimeError('Unexpected temporary directory; refusing recursive cleanup')
        for source in sources + sorted(ROOT.glob('include/*.svh')):
            destination = stage / source.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        (stage/'generated').mkdir()
        (stage/'generated/compile_matrix.sv').write_text(MATRIX, encoding='utf-8')
        (stage/'generated/uvm_stub.sv').write_text(UVM_STUB, encoding='utf-8')
        relative_sources = [source.relative_to(ROOT).as_posix() for source in sources]
        variants = [
            ('default', []),
            ('assertions_disabled', ['DV_SVA_DISABLE_ASSERTIONS']),
            ('covers_disabled', ['DV_SVA_DISABLE_COVERS']),
            ('uvm_report_signature', ['DV_SVA_USE_UVM']),
        ]
        try:
            os.chdir(stage)
            for name, defines in variants:
                preprocessor = PreprocessorOptions()
                preprocessor.additionalIncludePaths = ['include']
                preprocessor.predefines = defines
                options = pyslang.Bag()
                options.preprocessorOptions = preprocessor
                manager = pyslang.SourceManager()
                paths = relative_sources + ['generated/compile_matrix.sv']
                if name == 'uvm_report_signature':
                    paths = ['generated/uvm_stub.sv'] + paths
                tree = SyntaxTree.fromFiles(paths, manager, options)
                compilation = Compilation()
                compilation.addSyntaxTree(tree)
                diagnostics = list(compilation.getAllDiagnostics())
                rendered = pyslang.DiagnosticEngine.reportAll(manager, diagnostics)
                errors = sum(diagnostic.isError() for diagnostic in diagnostics)
                result = {'variant': name, 'errors': errors, 'diagnostic_count': len(diagnostics),
                          'diagnostics': rendered, 'passed': errors == 0}
                results.append(result)
                print(f'{name}: {errors} errors, {len(diagnostics)} diagnostics')
                if rendered:
                    print(rendered)
        finally:
            os.chdir(original_cwd)
    report = {'mode': 'static_only', 'actual_sva_simulations': False,
              'timestamp_utc': datetime.now(timezone.utc).isoformat(),
              'compiler': 'pyslang', 'compiler_version': pyslang.__version__,
              'source_files': [source.relative_to(ROOT).as_posix() for source in sources],
              'uvm_signature_stub_only': True, 'results': results}
    destination = ROOT/'build/static/compile_report.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Static report:', destination)
    print('No SVA simulation was performed. UVM adapter used a compile-only signature stub.')
    return 0 if all(result['passed'] for result in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())