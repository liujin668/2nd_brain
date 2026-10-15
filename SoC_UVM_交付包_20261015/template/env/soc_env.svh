class soc_env extends uvm_env;
  `uvm_component_utils(soc_env)
  soc_env_config cfg;
  soc_run_state state;
  soc_memory_driver driver;
  uvm_sequencer #(soc_mem_req) memory_sequencer;
  soc_tl_memory_backend backend;
  soc_tl_monitor monitor;
  soc_scoreboard scoreboard;
  soc_cov_collector coverage;
  soc_result_manager results;
  soc_virtual_sequencer virtual_sequencer;

  function new(string name, uvm_component parent); super.new(name, parent); endfunction
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (!uvm_config_db #(soc_env_config)::get(this, "", "cfg", cfg))
      `uvm_fatal("ENV_CONFIG_MISSING", "soc_env_config is required")
    cfg.validate();
    state = soc_run_state::type_id::create("state");
    driver = soc_memory_driver::type_id::create("driver", this);
    memory_sequencer =
      uvm_sequencer #(soc_mem_req)::type_id::create("memory_sequencer", this);
    backend = soc_tl_memory_backend::type_id::create("backend", this);
    monitor = soc_tl_monitor::type_id::create("monitor", this);
    scoreboard = soc_scoreboard::type_id::create("scoreboard", this);
    coverage = soc_cov_collector::type_id::create("coverage", this);
    results = soc_result_manager::type_id::create("results", this);
    virtual_sequencer =
      soc_virtual_sequencer::type_id::create("virtual_sequencer", this);
    driver.state = state;
    driver.backend = backend;
    backend.cfg = cfg;
    backend.state = state;
    monitor.state = state;
    scoreboard.state = state;
    coverage.state = state;
    results.cfg = cfg;
    results.state = state;
    virtual_sequencer.cfg = cfg;
    virtual_sequencer.state = state;
    virtual_sequencer.backend = backend;
    virtual_sequencer.scoreboard = scoreboard;
    virtual_sequencer.memory_sequencer = memory_sequencer;
  endfunction
  function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    driver.seq_item_port.connect(memory_sequencer.seq_item_export);
    driver.intent_ap.connect(scoreboard.expected_export);
    backend.completed_ap.connect(monitor.raw_export);
    monitor.observed_ap.connect(scoreboard.observed_export);
    monitor.observed_ap.connect(coverage.analysis_export);
  endfunction
  function void start_of_simulation_phase(uvm_phase phase);
    super.start_of_simulation_phase(phase);
    if (driver.intent_ap.size() != 1 || backend.completed_ap.size() != 1 ||
        monitor.observed_ap.size() != 2)
      `uvm_fatal("CHECKER_DISCONNECTED", "Required observation/check paths are absent")
  endfunction
  task run_phase(uvm_phase phase);
    forever begin
      @(negedge cfg.observe.rst_n);
      if (state.stage == SOC_RUNNING || state.stage == SOC_DRAINING)
        state.fail("UNEXPECTED_RUNTIME_RESET",
                   "This demo does not define outstanding-transaction reset recovery");
    end
  endtask
endclass
