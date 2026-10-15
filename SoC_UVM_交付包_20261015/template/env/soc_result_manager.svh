class soc_result_manager extends uvm_component;
  `uvm_component_utils(soc_result_manager)
  soc_env_config cfg;
  soc_run_state state;
  protected bit written = 0;
  function new(string name, uvm_component parent); super.new(name, parent); endfunction

  function string json_escape(string input_text);
    string output_text = "";
    byte unsigned c;
    for (int i = 0; i < input_text.len(); i++) begin
      c = input_text.getc(i);
      case (c)
        8'h22: output_text = {output_text, "\\\""};
        8'h5c: output_text = {output_text, "\\\\"};
        8'h0a: output_text = {output_text, "\\n"};
        8'h0d: output_text = {output_text, "\\r"};
        8'h09: output_text = {output_text, "\\t"};
        default:
          if (c < 8'h20)
            output_text = {output_text, $sformatf("\\u%04x", c)};
          else
            output_text = {output_text, input_text.substr(i, i)};
      endcase
    end
    return output_text;
  endfunction

  // Every component's check/report phase has finished before final phase.
  // Contract: other components must not add checks in final_phase or write JSON.
  function void final_phase(uvm_phase phase);
    uvm_report_server server;
    int unsigned errors, fatals, assertion_errors;
    int handle;
    bit passed;
    string status;
    super.final_phase(phase);
    if (written) begin
      `uvm_error("DUPLICATE_RESULT_WRITE", "Result manager invoked twice")
      return;
    end
    if (cfg == null || state == null)
      `uvm_fatal("RESULT_COMPONENT_MISSING", "Missing result config/state")
    server = uvm_report_server::get_server();
    errors = server.get_severity_count(UVM_ERROR);
    fatals = server.get_severity_count(UVM_FATAL);
    assertion_errors = cfg.assertions.errors;
    foreach (cfg.assertions.error_ids[i])
      state.record_failure(cfg.assertions.error_ids[i]);
    if (!state.completed || state.stage != SOC_DONE)
      state.record_failure("TEST_INCOMPLETE");
    if (state.stimulus_count == 0 || state.checks_count == 0 ||
        state.read_checks_count == 0)
      state.record_failure("ZERO_CHECKS");
    if (state.observed_count == 0 || state.coverage_samples == 0)
      state.record_failure("OBSERVATION_MISSING");
    if (state.stimulus_count != state.checks_count)
      state.record_failure("CHECK_COUNT_MISMATCH");
    if (state.pending_count != 0)
      state.record_failure("PENDING_TRANSACTIONS");
    if (errors != 0) state.record_failure("UVM_ERROR");
    if (fatals != 0) state.record_failure("UVM_FATAL");
    if (state.software_required && state.software_status != "PASS")
      state.record_failure("SOFTWARE_INCOMPLETE");
    passed = state.failures.size() == 0 && assertion_errors == 0;
    status = passed ? "PASS" : "FAIL";
    handle = $fopen(cfg.result_file, "w");
    if (handle == 0) begin
      `uvm_error("RESULT_FILE_OPEN",
        $sformatf("Cannot write result file %s", cfg.result_file))
      return; // Runner treats missing result as failure.
    end
    $fdisplay(handle, "{");
    $fdisplay(handle, "  \"schema_version\": %0d,", SOC_RESULT_SCHEMA_VERSION);
    $fdisplay(handle, "  \"run_id\": \"%s\",", json_escape(cfg.run_id));
    $fdisplay(handle, "  \"profile\": \"%s\",", json_escape(cfg.profile));
    $fdisplay(handle, "  \"test\": \"%s\",", json_escape(cfg.test_name));
    $fdisplay(handle, "  \"seed\": %0d,", cfg.seed);
    $fdisplay(handle, "  \"status\": \"%s\",", status);
    $fdisplay(handle, "  \"completed\": %s,", state.completed ? "true" : "false");
    $fdisplay(handle, "  \"stimulus_count\": %0d,", state.stimulus_count);
    $fdisplay(handle, "  \"checks_count\": %0d,", state.checks_count);
    $fdisplay(handle, "  \"pending_count\": %0d,", state.pending_count);
    $fdisplay(handle, "  \"uvm_errors\": %0d,", errors);
    $fdisplay(handle, "  \"uvm_fatals\": %0d,", fatals);
    $fdisplay(handle, "  \"assertion_errors\": %0d,", assertion_errors);
    $fdisplay(handle, "  \"software_required\": %s,",
              state.software_required ? "true" : "false");
    $fdisplay(handle, "  \"software_status\": \"%s\",",
              json_escape(state.software_status));
    $fwrite(handle, "  \"failures\": [");
    foreach (state.failures[i]) begin
      if (i != 0) $fwrite(handle, ", ");
      $fwrite(handle, "\"%s\"", json_escape(state.failures[i]));
    end
    $fdisplay(handle, "]");
    $fdisplay(handle, "}");
    $fclose(handle);
    written = 1;
    $display("SOC_RESULT_WRITTEN status=%s run_id=%s file=%s",
             status, cfg.run_id, cfg.result_file);
  endfunction
endclass
