interface soc_clk_ctrl_if;
  timeunit 1ps;
  timeprecision 1ps;
  bit request_enable = 0;
  time request_period = 10ns;
  int unsigned request_id = 0;
  int unsigned acknowledge_id; // Written only by soc_clk_gen.
  bit running;                 // Written only by soc_clk_gen.
  semaphore request_lock = new(1);

  task automatic set_clock(input bit enable, input time period);
    int unsigned mine;
    request_lock.get(1);
    request_enable = enable;
    request_period = period;
    request_id++;
    mine = request_id;
    wait (acknowledge_id == mine);
    request_lock.put(1);
  endtask
endinterface

interface soc_reset_ctrl_if;
  timeunit 1ps;
  timeprecision 1ps;
  bit request_assert = 1;
  int unsigned request_id = 0;
  int unsigned acknowledge_id; // Written only by soc_reset_gen.
  bit is_asserted;              // Written only by soc_reset_gen.
  semaphore request_lock = new(1);

  task automatic set_reset(input bit asserted);
    int unsigned mine;
    request_lock.get(1);
    request_assert = asserted;
    request_id++;
    mine = request_id;
    wait (acknowledge_id == mine);
    request_lock.put(1);
  endtask
endinterface

interface soc_observe_if(input logic clk, input logic rst_n);
  timeunit 1ps;
  timeprecision 1ps;
endinterface

interface soc_assert_status_if;
  timeunit 1ps;
  timeprecision 1ps;
  int unsigned errors = 0;
  int unsigned registered_count = 0;
  int unsigned samples = 0;
  string error_ids[$];

  function void register_checker();
    registered_count++;
  endfunction
  function void record_sample();
    samples++;
  endfunction

  // Static checkers use this API; the UVM result manager is the only JSON writer.
  // Do not terminate here: final reporting must preserve the failure evidence.
  task automatic note(input string id);
    errors++;
    error_ids.push_back(id);
    $display("SOC_ASSERTION_ERROR [%s] at %0t", id, $time);
  endtask
endinterface
