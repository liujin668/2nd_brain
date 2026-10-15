class soc_run_state extends uvm_object;
  `uvm_object_utils(soc_run_state)
  soc_stage_e stage = SOC_INIT;
  int unsigned epoch = 0;
  int unsigned stimulus_count = 0;
  int unsigned checks_count = 0;
  int unsigned read_checks_count = 0;
  int unsigned pending_count = 0;
  int unsigned observed_count = 0;
  int unsigned coverage_samples = 0;
  bit completed = 0;
  bit software_required = 0;
  string software_status = "NOT_REQUIRED";
  string failures[$];
  function new(string name = "soc_run_state"); super.new(name); endfunction
  function void record_failure(string id);
    foreach (failures[i]) if (failures[i] == id) return;
    failures.push_back(id);
  endfunction
  function void fail(string id, string message);
    record_failure(id);
    `uvm_error(id, message)
  endfunction
endclass
