// This is a CLOCK/RESET DEMONSTRATOR, not an AXI slave and not a SoC DUT.
// The memory selftest runs at the UVM transaction layer, outside this module.
module soc_demo_wrapper(input logic clk, input logic rst_n);
  timeunit 1ps;
  timeprecision 1ps;
  logic [7:0] cycle_marker;
  always_ff @(posedge clk or negedge rst_n)
    if (!rst_n) cycle_marker <= '0;
    else        cycle_marker <= cycle_marker + 1'b1;
endmodule
