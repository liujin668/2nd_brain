class soc_selftest extends uvm_test;
  `uvm_component_utils(soc_selftest)
  soc_env_config cfg;
  soc_env environment;
  function new(string name, uvm_component parent); super.new(name, parent); endfunction
  virtual function void customize_config(); cfg.inject_mismatch = 0; endfunction
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (!uvm_config_db #(soc_env_config)::get(this, "", "cfg", cfg))
      `uvm_fatal("TEST_CONFIG_MISSING", "Top must provide config before run_test")
    customize_config();
    uvm_config_db #(soc_env_config)::set(this, "environment", "cfg", cfg);
    environment = soc_env::type_id::create("environment", this);
  endfunction
  task run_phase(uvm_phase phase);
    soc_boot_memory_vseq sequence_body;
    phase.raise_objection(this);
    sequence_body = soc_boot_memory_vseq::type_id::create("sequence_body");
    fork
      begin
        sequence_body.start(environment.virtual_sequencer);
        environment.state.completed = 1;
      end
      begin
        #(cfg.timeout);
        environment.state.fail("SOC_TIMEOUT", "Selftest did not complete within simulation timeout");
      end
    join_any
    disable fork;
    phase.drop_objection(this);
  endtask
endclass

// Expected simulation outcome: FAIL with DATA_MISMATCH. This is an environment
// negative test, never a passing design test and never waived as a normal PASS.
class soc_selftest_mismatch extends soc_selftest;
  `uvm_component_utils(soc_selftest_mismatch)
  function new(string name, uvm_component parent); super.new(name, parent); endfunction
  virtual function void customize_config(); cfg.inject_mismatch = 1; endfunction
endclass
