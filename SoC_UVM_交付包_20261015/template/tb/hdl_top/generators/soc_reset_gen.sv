module soc_reset_gen(soc_reset_ctrl_if ctrl, output logic rst_n);
  timeunit 1ps;
  timeprecision 1ps;
  int unsigned seen;

  // This process is the ONLY owner of the external reset pin.
  // Domain synchronization is a DUT responsibility, not fabricated by this TB.
  initial begin
    rst_n = 0;
    seen = 0;
    ctrl.is_asserted = 1;
    ctrl.acknowledge_id = 0;
    forever begin
      wait (ctrl.request_id != seen);
      seen = ctrl.request_id;
      rst_n = !ctrl.request_assert;
      ctrl.is_asserted = ctrl.request_assert;
      ctrl.acknowledge_id = seen;
    end
  end
endmodule
