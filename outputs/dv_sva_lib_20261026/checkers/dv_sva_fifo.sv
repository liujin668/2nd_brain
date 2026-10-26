// FIFO occupancy/flag checks. This checker does not verify payload or ordering.
// 仅检查 FIFO 占用量、操作合法性和标志，不替代数据顺序 scoreboard。
`include "dv_sva_macros.svh"

module dv_sva_fifo #(
  parameter int unsigned DEPTH = 4,
  parameter int unsigned COUNT_WIDTH = (DEPTH < 1 ? 1 : $clog2(64'(DEPTH) + 64'd1)),
  parameter bit ALLOW_FULL_REPLACE = 1'b1,
  parameter bit ALLOW_EMPTY_BYPASS = 1'b0
) (
  input logic                   clk,
  input logic                   rst_n,
  input logic                   push_i,
  input logic                   pop_i,
  input logic                   full_i,
  input logic                   empty_i,
  input logic [COUNT_WIDTH-1:0] count_i
);

  // push_i/pop_i describe EXECUTED operations at this edge, not requests that
  // may be rejected by a full/empty FIFO. count_i is PRE-operation occupancy.
  // push/pop 为本拍执行事件；count_i 为该采样沿执行操作前的占用量。
  localparam int unsigned EXT_WIDTH = COUNT_WIDTH + 1;
  localparam logic [COUNT_WIDTH-1:0] DEPTH_COUNT = COUNT_WIDTH'(DEPTH);
  localparam logic [EXT_WIDTH-1:0] DEPTH_EXT = EXT_WIDTH'(DEPTH);

  initial begin : p_parameter_checks
    if (DEPTH < 1)
      $fatal(1, "dv_sva_fifo: DEPTH must be at least 1");
    if (COUNT_WIDTH < 1 || COUNT_WIDTH < $clog2(64'(DEPTH) + 64'd1))
      $fatal(1, "dv_sva_fifo: COUNT_WIDTH cannot represent all values 0..DEPTH");
  end

  `DV_SVA_KNOWN(a_control_known, ({push_i, pop_i, full_i, empty_i}))
  `DV_SVA_KNOWN(a_count_known, count_i)
  `DV_SVA_ASSERT(a_count_range, ({1'b0, count_i} <= DEPTH_EXT))
  `DV_SVA_ASSERT(a_full_flag, full_i == (count_i == DEPTH_COUNT))
  `DV_SVA_ASSERT(a_empty_flag, empty_i == (count_i == '0))

  // At full: replacing one popped item is configurable. At empty: simultaneous
  // push/pop is configurable bypass. Two executed operations keep count fixed.
  // 满时替换、空时直通分别配置；默认允许满时替换，不允许空时直通。
  `DV_SVA_ASSERT(a_no_overflow,
    (push_i && (count_i == DEPTH_COUNT))
      |-> (ALLOW_FULL_REPLACE && pop_i))
  `DV_SVA_ASSERT(a_no_underflow,
    (pop_i && (count_i == '0))
      |-> (ALLOW_EMPTY_BYPASS && push_i))

  // Widen before arithmetic to catch wrap-around rather than accepting it.
  // 增减两侧扩宽一位，避免计数器回绕与预期运算同时溢出而漏检。
  `DV_SVA_ASSERT(a_count_increment,
    (push_i && !pop_i && ({1'b0, count_i} < DEPTH_EXT))
      |=> ({1'b0, count_i} == ({1'b0, $past(count_i)} + 1'b1)))
  `DV_SVA_ASSERT(a_count_decrement,
    (!push_i && pop_i && (count_i > '0))
      |=> ({1'b0, count_i} == ({1'b0, $past(count_i)} - 1'b1)))
  `DV_SVA_ASSERT(a_count_stable,
    (push_i == pop_i) |=> $stable(count_i))

  `DV_SVA_COVER(c_empty, count_i == '0)
  `DV_SVA_COVER(c_full, count_i == DEPTH_COUNT)
  `DV_SVA_COVER(c_push_only, push_i && !pop_i)
  `DV_SVA_COVER(c_pop_only, !push_i && pop_i)
  `DV_SVA_COVER(c_push_and_pop, push_i && pop_i)

endmodule
