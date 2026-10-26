// Ready/valid source-side protocol checks; passive, single clock domain.
// 单时钟、被动检查：发生反压后，发送方必须保持 valid 与 payload。
`include "dv_sva_macros.svh"

module dv_sva_ready_valid #(
  parameter int unsigned DATA_WIDTH = 32,
  parameter bit CHECK_PAYLOAD_KNOWN = 1'b1
) (
  input logic                  clk,
  input logic                  rst_n,
  input logic                  valid_i,
  input logic                  ready_i,
  input logic [DATA_WIDTH-1:0] data_i
);
  timeunit 1ns;
  timeprecision 1ps;

  initial begin : p_parameter_checks
    if (DATA_WIDTH < 1)
      $fatal(1, "dv_sva_ready_valid: DATA_WIDTH must be at least 1");
  end

  // Check controls independently: an X antecedent must not hide a violation.
  // control 的 X/Z 独立检查；仅检查 valid 时的数据，不能代替此项。
  `DV_SVA_KNOWN(a_control_known, ({valid_i, ready_i}))

  if (CHECK_PAYLOAD_KNOWN) begin : g_payload_known
    `DV_SVA_ASSERT(a_data_known,
      valid_i |-> !$isunknown(data_i))
  end

  // Include the cycle that accepts the transfer: if the previous cycle stalled,
  // this cycle must still present the same valid/data, even when ready_i is 1.
  // 不增加 past_valid；非重叠蕴含的后件天然已有一拍历史。
  `DV_SVA_ASSERT(a_hold_on_stall,
    (valid_i && !ready_i) |=> (valid_i && $stable(data_i)))

  `DV_SVA_COVER(c_transfer, valid_i && ready_i)
  `DV_SVA_COVER(c_stall, valid_i && !ready_i)
  `DV_SVA_COVER(c_one_stall_then_transfer,
    (valid_i && !ready_i) ##1 (valid_i && ready_i))

endmodule
