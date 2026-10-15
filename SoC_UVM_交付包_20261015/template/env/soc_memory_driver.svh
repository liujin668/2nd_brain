class soc_memory_driver extends uvm_driver #(soc_mem_req);
  `uvm_component_utils(soc_memory_driver)
  soc_run_state state;
  soc_tl_memory_backend backend;
  uvm_analysis_port #(soc_mem_req) intent_ap;
  function new(string name, uvm_component parent);
    super.new(name, parent);
    intent_ap = new("intent_ap", this);
  endfunction
  task run_phase(uvm_phase phase);
    soc_mem_req request;
    forever begin
      seq_item_port.get_next_item(request);
      if (backend == null)
        `uvm_fatal("BACKEND_MISSING", "No transaction backend is connected")
      if (state.stage != SOC_RUNNING)
        state.fail("TRAFFIC_BEFORE_READY", "Traffic requires completed boot handshake");
      request.epoch = state.epoch;
      // Intent is recorded before execution so dropped completions remain pending.
      intent_ap.write(request);
      backend.execute(request);
      seq_item_port.item_done();
    end
  endtask
endclass
