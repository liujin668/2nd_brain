`include "dv_sva_macros.svh"

// Self-test stimulus, not synthesizable RTL. Run exactly one +CASE per simulation.
// Every stimulus transition occurs on a falling edge; assertions sample rising edges.
module dv_sva_tb;
  timeunit 1ns;
  timeprecision 1ps;

  logic clk = 1'b0;
  always #5ns clk = ~clk;

  string case_name;
  logic rv_rst_n, rv_valid, rv_ready;
  logic [7:0] rv_data;
  logic rsp_rst_n, req, rsp;
  logic fifo_rst_n, push, pop;
  logic [1:0] count;
  logic override_full, forced_full;
  wire full = override_full ? forced_full : (count == 2'd3);
  wire empty = (count == 2'd0);
  logic fifo1_rst_n, push1, pop1, count1;
  wire full1 = count1;
  wire empty1 = !count1;
  logic macro_rst_n, pulse_sig, known_enable;
  logic [7:0] known_sig, conditional_sig;
  logic [3:0] onehot_sig, onehot0_sig;

  dv_sva_ready_valid #(.DATA_WIDTH(8)) u_rv (
    .clk(clk), .rst_n(rv_rst_n), .valid_i(rv_valid),
    .ready_i(rv_ready), .data_i(rv_data)
  );
  dv_sva_response_window #(.MIN_CYCLES(1), .MAX_CYCLES(3)) u_rsp (
    .clk(clk), .rst_n(rsp_rst_n), .req_i(req), .rsp_i(rsp)
  );
  dv_sva_fifo #(.DEPTH(3), .COUNT_WIDTH(2)) u_fifo (
    .clk(clk), .rst_n(fifo_rst_n), .push_i(push), .pop_i(pop),
    .full_i(full), .empty_i(empty), .count_i(count)
  );
  dv_sva_fifo #(.DEPTH(1), .COUNT_WIDTH(1), .ALLOW_EMPTY_BYPASS(1)) u_fifo1 (
    .clk(clk), .rst_n(fifo1_rst_n), .push_i(push1), .pop_i(pop1),
    .full_i(full1), .empty_i(empty1), .count_i(count1)
  );

  `DV_SVA_KNOWN(a_test_known, known_sig, clk, macro_rst_n)
  `DV_SVA_KNOWN_WHEN(a_test_known_when, conditional_sig, known_enable, clk, macro_rst_n)
  `DV_SVA_ONEHOT(a_test_onehot, onehot_sig, clk, macro_rst_n)
  `DV_SVA_ONEHOT0(a_test_onehot0, onehot0_sig, clk, macro_rst_n)
  `DV_SVA_PULSE(a_test_pulse, pulse_sig, clk, macro_rst_n)

  task automatic tick(input int unsigned cycles = 1);
    repeat (cycles) @(negedge clk);
  endtask

  // Supply an explicit pre-operation occupancy rather than computing a DUT model.
  // The following call supplies the next sampled occupancy, testing the transition.
  task automatic fifo_sample(input bit p, input bit q, input logic [1:0] occupancy);
    push = p;
    pop = q;
    count = occupancy;
    tick();
  endtask

  task automatic run_rv_positive();
    rv_rst_n = 1'b1;
    rv_valid = 1'b1;
    rv_ready = 1'b0;
    rv_data = 8'hA5;
    tick(3);
    rv_ready = 1'b1;
    tick();
    rv_valid = 1'b0;
    tick(2);
    rv_rst_n = 1'b0;
  endtask

  task automatic run_response_minmax();
    rsp_rst_n = 1'b1;
    req = 1'b0;
    rsp = 1'b0;
    tick();
    req = 1'b1;
    tick();
    req = 1'b0;
    rsp = 1'b1; // MIN=1: first permitted response sample.
    tick();
    rsp = 1'b0;
    tick(3);
    req = 1'b1;
    tick();
    req = 1'b0;
    tick(2);
    rsp = 1'b1; // MAX=3: last permitted response sample.
    tick();
    rsp = 1'b0;
    tick(4);
    rsp_rst_n = 1'b0;
  endtask

  task automatic run_fifo_positive();
    fifo_rst_n = 1'b1;
    fifo_sample(1, 0, 0);
    fifo_sample(1, 0, 1);
    fifo_sample(1, 0, 2);
    fifo_sample(1, 1, 3); // Full replacement allowed; occupancy stays 3.
    fifo_sample(0, 1, 3);
    fifo_sample(0, 1, 2);
    fifo_sample(0, 1, 1);
    fifo_sample(0, 0, 0);
    fifo_sample(0, 0, 0);
    fifo_rst_n = 1'b0;
  endtask

  task automatic run_macro_positive();
    macro_rst_n = 1'b1;
    pulse_sig = 1'b1;
    tick();
    pulse_sig = 1'b0;
    onehot_sig = 4'b1000;
    onehot0_sig = 4'b0000;
    tick(2);
    macro_rst_n = 1'b0;
  endtask

  initial begin
    if (!$value$plusargs("CASE=%s", case_name)) case_name = "positive";
    rv_rst_n = 0; rv_valid = 0; rv_ready = 0; rv_data = 0;
    rsp_rst_n = 0; req = 0; rsp = 0;
    fifo_rst_n = 0; push = 0; pop = 0; count = 0;
    override_full = 0; forced_full = 0;
    fifo1_rst_n = 0; push1 = 0; pop1 = 0; count1 = 0;
    macro_rst_n = 0; pulse_sig = 0; known_enable = 1;
    known_sig = 8'h12; conditional_sig = 8'h34;
    onehot_sig = 4'b0001; onehot0_sig = 4'b0001;
    tick(2);
    $display("DV_SVA_CASE_START: %s", case_name);

    case (case_name)
      "positive": begin
        run_rv_positive();
        run_response_minmax();
        run_fifo_positive();
        run_macro_positive();
      end
      "rv_change_data": begin
        rv_rst_n = 1; rv_valid = 1; rv_ready = 0; rv_data = 8'hA5;
        tick();
        rv_ready = 1; rv_data = 8'h5A;
        tick();
        rv_valid = 0;
        tick(2);
      end
      "rv_drop_valid", "rv_first_after_reset": begin
        // The first active sample creates the obligation. No extra history guard.
        rv_rst_n = 1; rv_valid = 1; rv_ready = 0; rv_data = 8'hA5;
        tick();
        rv_valid = 0; rv_ready = 1;
        tick(2);
      end
      "response_timeout", "response_late", "response_same_cycle_only": begin
        rsp_rst_n = 1;
        tick();
        req = 1;
        rsp = (case_name == "response_same_cycle_only");
        tick();
        req = 0; rsp = 0;
        tick(3); // All of samples 1, 2, 3 have no response.
        if (case_name == "response_late") rsp = 1;
        tick(); // A response at sample 4 cannot satisfy the earlier request.
        rsp = 0;
        tick(2);
      end
      "response_minmax": run_response_minmax();
      "response_overlap_shared": begin
        // One response may satisfy both windows. This is intentionally NOT pairing.
        rsp_rst_n = 1;
        tick();
        req = 1; tick();
        req = 0; tick();
        req = 1; tick();
        req = 0; rsp = 1; tick();
        rsp = 0; tick(4);
      end
      "response_pending_end": begin
        rsp_rst_n = 1;
        tick();
        req = 1;
        tick();
        req = 0;
        // End before MAX; strong() must reject this still-pending obligation.
      end
      "fifo_overflow": begin
        count = 3; push = 1; fifo_rst_n = 1;
        tick();
        push = 0;
        tick(2);
      end
      "fifo_underflow": begin
        pop = 1; fifo_rst_n = 1;
        tick();
        pop = 0;
        tick(2);
      end
      "fifo_count": begin
        fifo_rst_n = 1;
        fifo_sample(1, 0, 0);
        fifo_sample(0, 0, 0); // Deliberately missing the accepted push increment.
        tick(2);
      end
      "fifo_flags": begin
        fifo_rst_n = 1; override_full = 1; forced_full = 1;
        tick();
        override_full = 0;
        tick(2);
      end
      "fifo_depth1": begin
        fifo1_rst_n = 1;
        push1 = 1; pop1 = 1; count1 = 0; tick(); // Empty bypass allowed.
        push1 = 1; pop1 = 0; count1 = 0; tick();
        push1 = 1; pop1 = 1; count1 = 1; tick(); // Full replacement allowed.
        push1 = 0; pop1 = 1; count1 = 1; tick();
        push1 = 0; pop1 = 0; count1 = 0; tick(2);
      end
      "pulse_wide": begin
        macro_rst_n = 1; pulse_sig = 1;
        tick(2);
        pulse_sig = 0;
        tick(2);
      end
      "onehot0_violation": begin
        macro_rst_n = 1; onehot0_sig = 4'b0011;
        tick();
        onehot0_sig = 4'b0000;
        tick(2);
      end
      "onehot_zero": begin
        macro_rst_n = 1; onehot_sig = 4'b0000;
        tick();
        onehot_sig = 4'b0001;
        tick(2);
      end
      "known_x": begin
        macro_rst_n = 1; known_sig = 'x;
        tick();
        known_sig = 8'h12;
        tick(2);
      end
      "known_when_x": begin
        macro_rst_n = 1; known_enable = 1; conditional_sig = 'x;
        tick();
        conditional_sig = 8'h34;
        tick(2);
      end
      "known_when_off": begin
        macro_rst_n = 1; known_enable = 0; conditional_sig = 'x;
        tick(2);
        conditional_sig = 8'h34; known_enable = 1;
        tick(2);
      end
      "control_x": begin
        rv_rst_n = 1; rv_valid = 1'bx; rv_ready = 0;
        tick();
        rv_valid = 0;
        tick(2);
      end
      "reset_unknown": begin
        macro_rst_n = 1'bx;
        known_sig = 'x; conditional_sig = 'x;
        onehot_sig = 'x; onehot0_sig = 'x; pulse_sig = 'x;
        tick(3); // 0/X/Z reset policy disables checks while reset is unknown.
        macro_rst_n = 0;
        known_sig = 8'h12; conditional_sig = 8'h34;
        onehot_sig = 4'b0001; onehot0_sig = 0; pulse_sig = 0;
        tick();
        macro_rst_n = 1;
        tick(3);
      end
      "reset_abort": begin
        rsp_rst_n = 1;
        tick();
        req = 1;
        tick(); // An obligation now exists.
        req = 0; rsp_rst_n = 0; // Mid-window asynchronous reset cancels it.
        tick(5);
        rsp_rst_n = 1;
        tick(4);
      end
      default: $fatal(1, "Unknown CASE: %s", case_name);
    endcase

    $display("DV_SVA_CASE_DONE: %s", case_name);
    $finish;
  end

  initial begin
    #10000ns;
    $fatal(1, "Self-test timeout");
  end
endmodule
