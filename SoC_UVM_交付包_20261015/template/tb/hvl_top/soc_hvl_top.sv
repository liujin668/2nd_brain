module soc_hvl_top;
  timeunit 1ps;
  timeprecision 1ps;
  import uvm_pkg::*;
  import soc_env_pkg::*;
  import soc_test_pkg::*;
  `include "uvm_macros.svh"
  `include "soc_tb_defines.svh"
  soc_env_config cfg;
  initial begin
    cfg = soc_env_config::type_id::create("cfg");
    cfg.load_plusargs();
    cfg.clk_ctrl = $root.soc_hdl_top.clk_ctrl;
    cfg.reset_ctrl = $root.soc_hdl_top.reset_ctrl;
    cfg.observe = $root.soc_hdl_top.observe;
    cfg.assertions = $root.soc_hdl_top.assert_status;
    // One ordered entry point: publish all handles BEFORE UVM build/run.
    uvm_config_db #(soc_env_config)::set(null, "uvm_test_top", "cfg", cfg);
    $display("SOC_TEMPLATE_VERSION=%s PROFILE=%s", `SOC_TEMPLATE_VERSION, cfg.profile);
    run_test();
  end
endmodule
