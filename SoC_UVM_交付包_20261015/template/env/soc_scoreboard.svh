`uvm_analysis_imp_decl(_expected)
`uvm_analysis_imp_decl(_observed)

class soc_scoreboard extends uvm_component;
  `uvm_component_utils(soc_scoreboard)
  soc_run_state state;
  soc_memory_reference reference;
  uvm_analysis_imp_expected #(soc_mem_req, soc_scoreboard) expected_export;
  uvm_analysis_imp_observed #(soc_mem_rsp, soc_scoreboard) observed_export;
  protected soc_mem_req pending[longint unsigned];

  function new(string name, uvm_component parent);
    super.new(name, parent);
    expected_export = new("expected_export", this);
    observed_export = new("observed_export", this);
    reference = soc_memory_reference::type_id::create("reference");
  endfunction
  function void reset_model(int unsigned epoch, bit preserve_memory);
    // Do not silently erase pending work. Mid-transaction reset semantics are
    // an explicit future adapter contract, not guessed by this selftest.
    if (pending.num() != 0)
      `uvm_fatal("RESET_PENDING_UNDEFINED", "Reset with pending traffic is unwired")
    state.epoch = epoch;
    reference.reset_model(preserve_memory);
  endfunction
  function void write_expected(soc_mem_req request);
    soc_mem_req snapshot;
    if (request == null)
      `uvm_fatal("NULL_REQUEST", "A null expected request is invalid")
    state.stimulus_count++;
    if (pending.exists(request.uid)) begin
      state.fail("DUPLICATE_REQUEST_ID", $sformatf("uid=%0d", request.uid));
      return;
    end
    if (!$cast(snapshot, request.clone()))
      `uvm_fatal("REQUEST_CLONE", "Cannot clone expected request")
    pending[request.uid] = snapshot;
    state.pending_count = pending.num();
  endfunction
  function void write_observed(soc_mem_rsp response);
    soc_mem_req request;
    soc_data_t wanted;
    if (!pending.exists(response.uid)) begin
      state.fail("UNEXPECTED_RESPONSE", $sformatf("uid=%0d", response.uid));
      return;
    end
    request = pending[response.uid];
    state.checks_count++;
    if (response.epoch != request.epoch || response.epoch != state.epoch)
      state.fail("RESET_EPOCH_MISMATCH", $sformatf("uid=%0d", response.uid));
    if (response.addr !== request.addr || response.op !== request.op ||
        response.byte_enable !== request.byte_enable)
      state.fail("RESPONSE_METADATA", $sformatf("uid=%0d", response.uid));
    if (response.error) begin
      state.fail("MEMORY_RESPONSE_ERROR", $sformatf("uid=%0d", response.uid));
    end else if (request.op == SOC_MEM_WRITE) begin
      reference.commit_write(request);
    end else begin
      wanted = reference.expected_read(request.addr);
      state.read_checks_count++;
      if (response.read_data !== wanted)
        state.fail("DATA_MISMATCH",
          $sformatf("uid=%0d addr=%016h expected=%016h observed=%016h",
                    response.uid, request.addr, wanted, response.read_data));
    end
    pending.delete(response.uid);
    state.pending_count = pending.num();
  endfunction
  function void check_phase(uvm_phase phase);
    super.check_phase(phase);
    if (pending.num() != 0)
      state.fail("PENDING_TRANSACTIONS", $sformatf("%0d pending", pending.num()));
    if (state.stimulus_count == 0 || state.read_checks_count == 0)
      state.fail("ZERO_CHECKS", "At least one request and checked read are required");
    if (state.stimulus_count != state.checks_count)
      state.fail("CHECK_COUNT_MISMATCH", "Every issued demo request needs a check");
  endfunction
endclass
