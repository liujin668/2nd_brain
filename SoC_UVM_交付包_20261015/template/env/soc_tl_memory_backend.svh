// Synthetic blocking transaction memory. This is NOT AXI, CHI, DDR or a CPU.
class soc_tl_memory_backend extends uvm_component;
  `uvm_component_utils(soc_tl_memory_backend)
  soc_env_config cfg;
  soc_run_state state;
  uvm_analysis_port #(soc_mem_rsp) completed_ap;
  protected logic [7:0] storage[soc_addr_t];
  protected bit corruption_injected = 0;

  function new(string name, uvm_component parent);
    super.new(name, parent);
    completed_ap = new("completed_ap", this);
  endfunction
  function void reset_model(bit preserve_memory);
    if (!preserve_memory) storage.delete();
    corruption_injected = 0;
  endfunction
  function void preload_word(soc_addr_t address, soc_data_t value);
    // Called only while the selftest reset is asserted, before any requests.
    if ($isunknown({address, value}))
      `uvm_fatal("PRELOAD_UNKNOWN", "Preload address/data must be fully known")
    if (cfg.observe.rst_n !== 1'b0)
      `uvm_fatal("PRELOAD_ORDER", "Preload requires asserted reset in selftest")
    for (int lane = 0; lane < 8; lane++)
      storage[address + lane] = value[lane*8 +: 8];
  endfunction

  task execute(soc_mem_req request);
    soc_mem_rsp response;
    response = soc_mem_rsp::type_id::create("response");
    response.op = request.op;
    response.addr = request.addr;
    response.data = request.data;
    response.byte_enable = request.byte_enable;
    response.uid = request.uid;
    response.epoch = request.epoch;
    response.read_data = '0;
    response.error = 0;
    @(posedge cfg.observe.clk);
    if ($isunknown({request.op, request.addr, request.byte_enable})) begin
      state.fail("REQUEST_CONTROL_UNKNOWN", "Unknown operation/address/byte-enable");
      response.error = 1;
    end else if (cfg.observe.rst_n !== 1'b1 ||
        request.addr < cfg.mem_base ||
        request.addr > cfg.mem_base + cfg.mem_bytes - 8 ||
        request.addr[2:0] != 0) begin
      response.error = 1;
    end else if (request.op == SOC_MEM_WRITE) begin
      // Reject unknown VALID bytes before any partial write is committed.
      for (int lane = 0; lane < 8; lane++)
        if (request.byte_enable[lane] &&
            $isunknown(request.data[lane*8 +: 8])) begin
          state.fail("REQUEST_DATA_UNKNOWN", "Unknown data in an enabled write byte");
          response.error = 1;
        end
      if (!response.error)
        for (int lane = 0; lane < 8; lane++)
          if (request.byte_enable[lane])
            storage[request.addr + lane] = request.data[lane*8 +: 8];
    end else begin
      for (int lane = 0; lane < 8; lane++)
        if (storage.exists(request.addr + lane))
          response.read_data[lane*8 +: 8] = storage[request.addr + lane];
      // Corrupt only the observed read response, not the reference model.
      if (cfg.inject_mismatch && !corruption_injected) begin
        response.read_data[0] = ~response.read_data[0];
        corruption_injected = 1;
      end
    end
    completed_ap.write(response);
  endtask
endclass
