module soc_clk_gen(soc_clk_ctrl_if ctrl,
                   soc_assert_status_if assertions,
                   output logic clk);
  timeunit 1ps;
  timeprecision 1ps;
  bit enabled;
  time period;
  int unsigned seen;

  // This process is the ONLY owner of clk. Requests are accepted while clk=0;
  // a stop or period change never cuts a high pulse short.
  initial begin
    clk = 0;
    enabled = 0;
    period = 10ns;
    seen = 0;
    ctrl.acknowledge_id = 0;
    ctrl.running = 0;
    forever begin
      if (!enabled)
        wait (ctrl.request_id != seen);
      if (ctrl.request_id != seen) begin
        seen = ctrl.request_id;
        if (ctrl.request_enable && ctrl.request_period < 2ps) begin
          // All time-valued controls use integral ps in this template.
          // A period needs at least two precision ticks for two nonzero phases.
          assertions.note("CLK_PERIOD_UNSUPPORTED");
          enabled = 0;
        end else begin
          enabled = ctrl.request_enable;
          period = ctrl.request_period;
        end
        ctrl.running = enabled;
        ctrl.acknowledge_id = seen;
      end
      if (enabled) begin
        #(period / 2) clk = 1;
        #(period - period / 2) clk = 0;
      end
    end
  end
endmodule
