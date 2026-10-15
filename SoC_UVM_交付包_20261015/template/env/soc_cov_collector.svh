class soc_cov_collector extends uvm_subscriber #(soc_mem_rsp);
  `uvm_component_utils(soc_cov_collector)
  soc_run_state state;
  covergroup memory_cg with function sample(bit is_write, bit [7:0] mask, bit error);
    option.per_instance = 1;
    cp_op: coverpoint is_write {bins read_op = {0}; bins write_op = {1};}
    cp_mask: coverpoint mask iff (is_write) {
      bins full = {8'hff}; bins none = {8'h00}; bins partial = default;
    }
    cp_error: coverpoint error {bins ok = {0}; bins failed = {1};}
  endgroup
  function new(string name, uvm_component parent);
    super.new(name, parent);
    memory_cg = new;
  endfunction
  function void write(soc_mem_rsp t);
    memory_cg.sample(t.op == SOC_MEM_WRITE, t.byte_enable, t.error);
    state.coverage_samples++;
  endfunction
endclass
