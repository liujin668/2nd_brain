module soc_pin_checks(input logic clk, input logic rst_n,
                      input logic [7:0] cycle_marker,
                      soc_assert_status_if status);
  timeunit 1ps;
  timeprecision 1ps;

  initial status.register_checker();
  always @(posedge clk) status.record_sample();

  a_reset_known: assert property (@(posedge clk) !$isunknown(rst_n))
    else status.note("RESET_UNKNOWN");
  a_reset_effect: assert property (@(posedge clk)
      ((rst_n === 1'b0) && ($past(rst_n) === 1'b0))
        |-> (cycle_marker === 8'h00))
    else status.note("RESET_EFFECT");
  a_marker_known: assert property (@(posedge clk)
      disable iff (rst_n !== 1'b1) !$isunknown(cycle_marker))
    else status.note("DEMO_MARKER_UNKNOWN");
  c_reset_seen: cover property (@(posedge clk) rst_n === 1'b0);
  c_run_seen: cover property (@(posedge clk) rst_n === 1'b1);
endmodule
