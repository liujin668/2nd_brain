`ifndef DV_SVA_MACROS_SVH
`define DV_SVA_MACROS_SVH

// dv_sva_lib 0.1.0
// Contract: CLK is a one-bit clock; RST_N is active-low.
// rst_n = 0/X/Z cancels in-flight attempts. This is an explicit policy;
// it does NOT assert that reset itself is known.
// Calls expand to complete declarations: do not add a trailing semicolon.
// Pass comma-containing expressions inside an extra pair of parentheses.

`define DV_SVA_STRINGIFY(TEXT) `"TEXT`"

// An integrator may define DV_SVA_REPORT_ERROR before including this file.
// Keep the DV_SVA_FAIL <ID> prefix if using the supplied regression runner.
`ifndef DV_SVA_REPORT_ERROR
  `ifdef DV_SVA_USE_UVM
    `define DV_SVA_REPORT_ERROR(NAME, MESSAGE) \
      uvm_pkg::uvm_report_error("SVA", \
        $sformatf("DV_SVA_FAIL %s | %m | %s", \
          `DV_SVA_STRINGIFY(NAME), MESSAGE), \
        uvm_pkg::UVM_NONE, `__FILE__, `__LINE__);
  `else
    `define DV_SVA_REPORT_ERROR(NAME, MESSAGE) \
      $error("DV_SVA_FAIL %s | %m | %s", \
        `DV_SVA_STRINGIFY(NAME), MESSAGE);
  `endif
`endif

// Disable only by deliberate build configuration, never by simulator name.
// The regression runner must not be used with assertions disabled.
`ifdef DV_SVA_DISABLE_ASSERTIONS
  `define DV_SVA_ASSERT_MSG(NAME, PROP, MESSAGE, CLK=clk, RST_N=rst_n)
`else
  `define DV_SVA_ASSERT_MSG(NAME, PROP, MESSAGE, CLK=clk, RST_N=rst_n) \
    NAME: assert property (@(posedge (CLK)) \
      disable iff ((RST_N) !== 1'b1) (PROP)) \
      else begin \
        `DV_SVA_REPORT_ERROR(NAME, MESSAGE) \
      end
`endif

`define DV_SVA_ASSERT(NAME, PROP, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, PROP, "property violated", CLK, RST_N)

`ifdef DV_SVA_DISABLE_COVERS
  `define DV_SVA_COVER(NAME, SEQ, CLK=clk, RST_N=rst_n)
`else
  `define DV_SVA_COVER(NAME, SEQ, CLK=clk, RST_N=rst_n) \
    NAME: cover property (@(posedge (CLK)) \
      disable iff ((RST_N) !== 1'b1) (SEQ));
`endif

// Known checks need a four-state simulator to verify X/Z failure cases.
`define DV_SVA_KNOWN(NAME, SIGNAL, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, !$isunknown(SIGNAL), \
    "signal contains X/Z", CLK, RST_N)

// ENABLE must be checked separately if it can be unknown.
`define DV_SVA_KNOWN_WHEN(NAME, SIGNAL, ENABLE, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, (ENABLE) |-> !$isunknown(SIGNAL), \
    "enabled signal contains X/Z", CLK, RST_N)

// $onehot/$onehot0 alone do not replace an explicit X/Z check.
`define DV_SVA_ONEHOT(NAME, SIGNAL, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, (!$isunknown(SIGNAL) && $onehot(SIGNAL)), \
    "expected exactly one known high bit", CLK, RST_N)

`define DV_SVA_ONEHOT0(NAME, SIGNAL, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, (!$isunknown(SIGNAL) && $onehot0(SIGNAL)), \
    "expected at most one known high bit", CLK, RST_N)

// Sampled pulse width: every sampled high must be followed by sampled low.
// This does not detect sub-cycle glitches or require physical pulse width.
// No blanket history-valid gate: the first post-reset sample is checked.
`define DV_SVA_PULSE(NAME, SIGNAL, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, \
    (!$isunknown(SIGNAL)) and ((SIGNAL) |=> !(SIGNAL)), \
    "pulse contains X/Z or stays high for consecutive samples", CLK, RST_N)

// Per sampled high antecedent, require the consequent one sample later.
// These convenience checks do not imply transaction pairing.
`define DV_SVA_NEXT(NAME, ANTECEDENT, CONSEQUENT, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT(NAME, (ANTECEDENT) |=> (CONSEQUENT), CLK, RST_N)

// Caller separately checks VALID/READY and active payload for X/Z.
`define DV_SVA_HOLD_WHEN_STALLED(NAME, VALID, READY, DATA, CLK=clk, RST_N=rst_n) \
  `DV_SVA_ASSERT_MSG(NAME, \
    ((VALID) && !(READY)) |=> ((VALID) && $stable(DATA)), \
    "valid or payload changed after a stalled sample", CLK, RST_N)

// Immediate invariant: no clock/reset behavior is implied.
`ifdef DV_SVA_DISABLE_ASSERTIONS
  `define DV_SVA_ASSERT_IMMEDIATE(NAME, EXPR)
`else
  `define DV_SVA_ASSERT_IMMEDIATE(NAME, EXPR) \
    NAME: assert (EXPR) \
      else begin \
        `DV_SVA_REPORT_ERROR(NAME, "immediate assertion violated") \
      end
`endif

`endif // DV_SVA_MACROS_SVH
