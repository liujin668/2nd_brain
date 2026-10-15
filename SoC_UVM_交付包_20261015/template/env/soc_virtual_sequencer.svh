class soc_virtual_sequencer extends uvm_sequencer #(uvm_sequence_item);
  `uvm_component_utils(soc_virtual_sequencer)
  soc_env_config cfg;
  soc_run_state state;
  soc_tl_memory_backend backend;
  soc_scoreboard scoreboard;
  uvm_sequencer #(soc_mem_req) memory_sequencer;
  function new(string name, uvm_component parent); super.new(name, parent); endfunction
endclass
