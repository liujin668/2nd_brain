class soc_env_config extends uvm_object;
  `uvm_object_utils(soc_env_config)
  string profile = "uvm_selftest";
  string run_id;
  string result_file;
  string test_name;
  int unsigned seed;
  bit inject_mismatch = 0;
  time timeout = 100us;
  soc_addr_t mem_base = SELFTEST_MEM_BASE;
  int unsigned mem_bytes = SELFTEST_MEM_BYTES;
  virtual soc_clk_ctrl_if clk_ctrl;
  virtual soc_reset_ctrl_if reset_ctrl;
  virtual soc_observe_if observe;
  virtual soc_assert_status_if assertions;

  function new(string name = "soc_env_config");
    super.new(name);
  endfunction

  function void load_plusargs();
    if (!$value$plusargs("SOC_PROFILE=%s", profile)) profile = "uvm_selftest";
    if (!$value$plusargs("SOC_RUN_ID=%s", run_id) || run_id.len() == 0)
      `uvm_fatal("RUN_ID_MISSING", "+SOC_RUN_ID is required")
    if (!$value$plusargs("SOC_RESULT_FILE=%s", result_file) ||
        result_file.len() == 0)
      `uvm_fatal("RESULT_PATH_MISSING", "+SOC_RESULT_FILE is required")
    if (!$value$plusargs("SOC_SEED=%d", seed))
      `uvm_fatal("SEED_MISSING", "+SOC_SEED is required")
    if (!$value$plusargs("UVM_TESTNAME=%s", test_name))
      `uvm_fatal("TEST_NAME_MISSING", "+UVM_TESTNAME is required")
  endfunction

  function void validate();
    if (profile != "uvm_selftest")
      `uvm_fatal("ADAPTER_UNWIRED",
        $sformatf("Profile %s has no real DUT/VIP/CPU adapter in this template",
                  profile))
    if (clk_ctrl == null || reset_ctrl == null || observe == null ||
        assertions == null)
      `uvm_fatal("CONTROL_IF_MISSING", "All control/observation VIFs are required")
    if ($isunknown(mem_base) || mem_bytes < 256 || mem_base[2:0] != 0)
      `uvm_fatal("MEMORY_CONFIG", "Selftest needs an aligned >=256-byte window")
  endfunction
endclass
