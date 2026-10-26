// A one-entry registered ready/valid stage for the bind example.
module demo_pipe #(parameter int unsigned DATA_WIDTH = 8) (
  input logic clk, rst_n,
  input logic in_valid,
  output logic in_ready,
  input logic [DATA_WIDTH-1:0] in_data,
  output logic out_valid,
  input logic out_ready,
  output logic [DATA_WIDTH-1:0] out_data
);
  timeunit 1ns;
  timeprecision 1ps;
  assign in_ready = !out_valid || out_ready;
  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      out_valid <= 1'b0;
      out_data <= '0;
    end else if (in_ready) begin
      out_valid <= in_valid;
      if (in_valid) out_data <= in_data;
    end
  end
endmodule
