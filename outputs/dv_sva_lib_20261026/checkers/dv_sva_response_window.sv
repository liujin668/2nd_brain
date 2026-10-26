// A bounded response-LEVEL window, not a transaction pairing scoreboard.
// 响应电平窗口：允许重叠请求共用一次响应，不检查响应与请求一一匹配。
`include "dv_sva_macros.svh"

module dv_sva_response_window #(
  parameter int MIN_CYCLES = 1,
  parameter int MAX_CYCLES = 8,
  parameter bit TRIGGER_ON_RISE = 1'b1
) (
  input logic clk,
  input logic rst_n,
  input logic req_i,
  input logic rsp_i
);

  initial begin : p_parameter_checks
    if (MIN_CYCLES < 0 || MAX_CYCLES < MIN_CYCLES)
      $fatal(1, "dv_sva_response_window: require 0 <= MIN_CYCLES <= MAX_CYCLES");
  end

  `DV_SVA_KNOWN(a_control_known, ({req_i, rsp_i}))

  // MIN_CYCLES=0 allows a response on the triggering sample. Rise mode starts
  // one attempt per sampled req rising edge; level mode starts one per high
  // sample. An early response does not itself fail, but a response LEVEL must
  // occur inside the inclusive window. Strong requires completion at test end.
  // MIN/MAX 均为静态周期数；strong 防止仿真结束时未完成义务静默通过。
  `DV_SVA_ASSERT(a_response_window,
    (TRIGGER_ON_RISE ? $rose(req_i) : req_i)
      |-> strong(##[MIN_CYCLES:MAX_CYCLES] rsp_i))

  `DV_SVA_COVER(c_request,
    (TRIGGER_ON_RISE ? $rose(req_i) : req_i))
  `DV_SVA_COVER(c_response_in_window,
    (TRIGGER_ON_RISE ? $rose(req_i) : req_i)
      ##[MIN_CYCLES:MAX_CYCLES] rsp_i)

endmodule
