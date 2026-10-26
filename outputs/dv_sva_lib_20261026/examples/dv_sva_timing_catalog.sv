// Copyable timing examples. Instantiate ONLY the rule(s) your protocol requires.
// These are teaching templates, not an additional mandatory protocol checker.
// Cycles refer to sampled posedges. Default reset policy is 0/X/Z disables.
`include "dv_sva_macros.svh"

module dv_sva_example_same_cycle(input logic clk, rst_n, a, b);
  timeunit 1ns; timeprecision 1ps;
  `DV_SVA_KNOWN(a_control_known, ({a, b}))
  `DV_SVA_ASSERT(a_same_cycle, a |-> b)
endmodule

module dv_sva_example_next_cycle(input logic clk, rst_n, a, b);
  timeunit 1ns; timeprecision 1ps;
  `DV_SVA_KNOWN(a_control_known, ({a, b}))
  `DV_SVA_ASSERT(a_next_cycle, a |=> b)
endmodule

module dv_sva_example_after_n #(parameter int N = 3)
  (input logic clk, rst_n, a, b);
  timeunit 1ns; timeprecision 1ps;
  initial if (N < 0) $fatal(1, "N must be >= 0");
  `DV_SVA_KNOWN(a_control_known, ({a, b}))
  // B must be high at N; B before N is not prohibited.
  `DV_SVA_ASSERT(a_after_n, a |-> strong(##N b))
endmodule

module dv_sva_example_window #(parameter int MIN = 1, MAX = 4)
  (input logic clk, rst_n, req, ack);
  timeunit 1ns; timeprecision 1ps;
  initial if (MIN < 0 || MAX < MIN) $fatal(1, "Require 0 <= MIN <= MAX");
  `DV_SVA_KNOWN(a_control_known, ({req, ack}))
  // Sampled rising edge trigger; response LEVEL window, not transaction pairing.
  `DV_SVA_ASSERT(a_window, $rose(req) |-> strong(##[MIN:MAX] ack))
  `DV_SVA_COVER(c_window_exercised, $rose(req) ##[MIN:MAX] ack)
endmodule

module dv_sva_example_rise_trigger(input logic clk, rst_n, a, b);
  timeunit 1ns; timeprecision 1ps;
  `DV_SVA_KNOWN(a_control_known, ({a, b}))
  `DV_SVA_ASSERT(a_rise_next, $rose(a) |=> b)
endmodule

module dv_sva_example_pulse(input logic clk, rst_n, pulse);
  timeunit 1ns; timeprecision 1ps;
  // Known check plus every sampled high followed by sampled low.
  `DV_SVA_PULSE(a_pulse, pulse)
endmodule

module dv_sva_example_stall #(parameter int WIDTH = 8)
  (input logic clk, rst_n, valid, ready, input logic [WIDTH-1:0] data);
  timeunit 1ns; timeprecision 1ps;
  initial if (WIDTH < 1) $fatal(1, "WIDTH must be >= 1");
  `DV_SVA_KNOWN(a_control_known, ({valid, ready}))
  `DV_SVA_KNOWN_WHEN(a_payload_known, data, valid)
  `DV_SVA_ASSERT(a_hold_on_stall, valid && !ready |=> valid && $stable(data))
endmodule

module dv_sva_example_busy_run #(parameter int N = 3)
  (input logic clk, rst_n, start, busy);
  timeunit 1ns; timeprecision 1ps;
  initial if (N < 1) $fatal(1, "N must be >= 1");
  `DV_SVA_KNOWN(a_control_known, ({start, busy}))
  // Start at C0 -> busy C1..CN, low at C(N+1). Not a complete start/busy protocol.
  `DV_SVA_ASSERT(a_busy_n_then_low, start |=> strong(busy[*N] ##1 !busy))
endmodule

module dv_sva_example_register #(parameter int WIDTH = 8)
  (input logic clk, rst_n, load, input logic [WIDTH-1:0] d, q);
  timeunit 1ns; timeprecision 1ps;
  initial if (WIDTH < 1) $fatal(1, "WIDTH must be >= 1");
  `DV_SVA_KNOWN(a_load_known, load)
  `DV_SVA_KNOWN_WHEN(a_input_known, d, load)
  // The consequent has a predecessor sample naturally; no blanket past_valid gate.
  `DV_SVA_ASSERT(a_capture_previous_d, load |=> q == $past(d))
endmodule
