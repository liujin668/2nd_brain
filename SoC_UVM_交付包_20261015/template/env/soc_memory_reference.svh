// Independent expected-data store. Never reads the backend's backing memory.
// The serialization rules below apply ONLY to the transaction-layer demo.
class soc_memory_reference extends uvm_object;
  `uvm_object_utils(soc_memory_reference)
  protected logic [7:0] expected[soc_addr_t];
  function new(string name = "soc_memory_reference"); super.new(name); endfunction
  function void reset_model(bit preserve_memory);
    if (!preserve_memory) expected.delete();
  endfunction
  function void initialize_word(soc_addr_t address, soc_data_t value);
    if ($isunknown({address, value}))
      `uvm_fatal("REFERENCE_PRELOAD_UNKNOWN", "Reference preload must be fully known")
    for (int lane = 0; lane < 8; lane++)
      expected[address + lane] = value[lane*8 +: 8];
  endfunction
  function void commit_write(soc_mem_req request);
    for (int lane = 0; lane < 8; lane++)
      if (request.byte_enable[lane])
        expected[request.addr + lane] = request.data[lane*8 +: 8];
  endfunction
  function soc_data_t expected_read(soc_addr_t address);
    soc_data_t value = '0;
    for (int lane = 0; lane < 8; lane++)
      if (expected.exists(address + lane))
        value[lane*8 +: 8] = expected[address + lane];
    return value;
  endfunction
endclass
