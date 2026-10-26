module tb_bind_example;
  timeunit 1ns;
  timeprecision 1ps;
  logic clk = 1'b0;
  always #5ns clk = ~clk;
  logic rst_n = 1'b0;
  logic in_valid = 1'b0;
  logic in_ready;
  logic [7:0] in_data = '0;
  logic out_valid;
  logic out_ready = 1'b0;
  logic [7:0] out_data;
  demo_pipe u_dut (.*);
  initial begin
    repeat (2) @(negedge clk);
    rst_n = 1'b1;
    in_valid = 1'b1;
    in_data = 8'hA5;
    @(negedge clk);
    in_valid = 1'b0;
    repeat (3) @(negedge clk);
    out_ready = 1'b1;
    repeat (3) @(negedge clk);
    $display("DV_SVA_CASE_DONE: bind_example");
    $finish;
  end
  initial begin
    #1us;
    $fatal(1, "bind example timeout");
  end
endmodule
