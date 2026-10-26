`include "dv_sva_macros.svh"

// Copy this module as a starting point for project-specific rules.
// Keep native SVA visible; the macros only supply clock/reset/reporting.
module dv_sva_custom_rules (
  input logic       clk,
  input logic       rst_n,
  input logic       req_i,
  input logic       ack_i,
  input logic [3:0] grant_i,
  input logic       pulse_i
);
  timeunit 1ns;
  timeprecision 1ps;

  `DV_SVA_KNOWN(a_control_known, ({req_i, ack_i}))
  `DV_SVA_NEXT(a_ack_next_sample, req_i, ack_i)
  `DV_SVA_ONEHOT0(a_grant_onehot0, grant_i)
  `DV_SVA_PULSE(a_single_sample_pulse, pulse_i)

  // An actual exercised path, rather than the vacuous success of implication.
  `DV_SVA_COVER(c_req_ack_exercised, req_i ##1 ack_i)
endmodule
