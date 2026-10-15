class soc_mem_req extends uvm_sequence_item;
  soc_mem_op_e op;
  soc_addr_t addr;
  soc_data_t data;
  bit [7:0] byte_enable;
  longint unsigned uid;
  int unsigned epoch;
  `uvm_object_utils_begin(soc_mem_req)
    `uvm_field_enum(soc_mem_op_e, op, UVM_ALL_ON)
    `uvm_field_int(addr, UVM_ALL_ON)
    `uvm_field_int(data, UVM_ALL_ON)
    `uvm_field_int(byte_enable, UVM_ALL_ON)
    `uvm_field_int(uid, UVM_ALL_ON)
    `uvm_field_int(epoch, UVM_ALL_ON)
  `uvm_object_utils_end
  function new(string name = "soc_mem_req"); super.new(name); endfunction
endclass

class soc_mem_rsp extends soc_mem_req;
  soc_data_t read_data;
  bit error;
  `uvm_object_utils_begin(soc_mem_rsp)
    `uvm_field_int(read_data, UVM_ALL_ON)
    `uvm_field_int(error, UVM_ALL_ON)
  `uvm_object_utils_end
  function new(string name = "soc_mem_rsp"); super.new(name); endfunction
endclass
