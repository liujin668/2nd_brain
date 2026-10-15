module soc_hdl_top;
  timeunit 1ps;
  timeprecision 1ps;
  logic clk;
  logic rst_n;
  soc_clk_ctrl_if clk_ctrl();
  soc_reset_ctrl_if reset_ctrl();
  soc_assert_status_if assert_status();
  soc_observe_if observe(clk, rst_n);
  soc_clk_gen u_clk_gen(clk_ctrl, assert_status, clk);
  soc_reset_gen u_reset_gen(reset_ctrl, rst_n);
  soc_demo_wrapper u_clock_reset_demo(clk, rst_n);
endmodule
