class soc_one_memory_access extends uvm_sequence #(soc_mem_req);
  `uvm_object_utils(soc_one_memory_access)
  soc_mem_op_e op;
  soc_addr_t addr;
  soc_data_t data;
  bit [7:0] byte_enable;
  longint unsigned uid;
  function new(string name = "soc_one_memory_access"); super.new(name); endfunction
  task body();
    soc_mem_req request = soc_mem_req::type_id::create("request");
    start_item(request);
    request.op = op;
    request.addr = addr;
    request.data = data;
    request.byte_enable = byte_enable;
    request.uid = uid;
    finish_item(request);
  endtask
endclass

class soc_boot_memory_vseq extends uvm_sequence #(uvm_sequence_item);
  `uvm_object_utils(soc_boot_memory_vseq)
  `uvm_declare_p_sequencer(soc_virtual_sequencer)
  protected longint unsigned uid = 0;
  protected longint unsigned rng;
  function new(string name = "soc_boot_memory_vseq"); super.new(name); endfunction

  function soc_data_t next_data();
    // Local deterministic PRNG: replay does not depend on unrelated UVM objects.
    rng ^= rng << 13;
    rng ^= rng >> 7;
    rng ^= rng << 17;
    return soc_data_t'(rng);
  endfunction
  task access(soc_mem_op_e operation, soc_addr_t address,
              soc_data_t value = '0, bit [7:0] mask = 8'hff);
    soc_one_memory_access operation_sequence;
    operation_sequence = soc_one_memory_access::type_id::create("access");
    operation_sequence.op = operation;
    operation_sequence.addr = address;
    operation_sequence.data = value;
    operation_sequence.byte_enable = mask;
    operation_sequence.uid = ++uid;
    operation_sequence.start(p_sequencer.memory_sequencer);
  endtask
  task body();
    soc_data_t initial_value;
    bit [7:0] mask;
    time first_edge;
    if (p_sequencer == null || p_sequencer.cfg == null ||
        p_sequencer.backend == null || p_sequencer.scoreboard == null ||
        p_sequencer.memory_sequencer == null)
      `uvm_fatal("SEQUENCER_WIRING", "Boot services are not connected")
    rng = 64'h9e3779b97f4a7c15 ^ soc_data_t'(p_sequencer.cfg.seed);
    p_sequencer.state.stage = SOC_RESET;
    p_sequencer.cfg.reset_ctrl.set_reset(1);
    p_sequencer.cfg.clk_ctrl.set_clock(1, 10ns);
    repeat (3) @(posedge p_sequencer.cfg.observe.clk);
    first_edge = $time;
    @(posedge p_sequencer.cfg.observe.clk);
    if (($time - first_edge) != 10ns)
      p_sequencer.state.fail("CLOCK_PERIOD_MISMATCH",
        $sformatf("Expected 10ns, observed %0t", $time - first_edge));
    p_sequencer.backend.reset_model(0);
    p_sequencer.scoreboard.reset_model(p_sequencer.state.epoch + 1, 0);
    // Fixed data supplied independently to actual and expected stores.
    // This is data preload only; it does not execute an ELF or boot a CPU.
    for (int i = 0; i < 8; i++) begin
      initial_value = 64'h1020304050607080 ^ soc_data_t'(i);
      p_sequencer.backend.preload_word(p_sequencer.cfg.mem_base + i*8,
                                      initial_value);
      p_sequencer.scoreboard.reference.initialize_word(
        p_sequencer.cfg.mem_base + i*8, initial_value);
    end
    // A deliberate safe edge for this demo's external reset release.
    // Real external reset timing must follow the actual pin specification.
    @(negedge p_sequencer.cfg.observe.clk);
    p_sequencer.cfg.reset_ctrl.set_reset(0);
    p_sequencer.state.stage = SOC_READY;
    repeat (2) @(posedge p_sequencer.cfg.observe.clk);
    p_sequencer.state.stage = SOC_RUNNING;
    for (int i = 0; i < 8; i++)
      access(SOC_MEM_READ, p_sequencer.cfg.mem_base + i*8);
    for (int i = 0; i < 16; i++) begin
      access(SOC_MEM_WRITE, p_sequencer.cfg.mem_base + i*8, next_data());
      access(SOC_MEM_READ, p_sequencer.cfg.mem_base + i*8);
      case (i % 4)
        0: mask = 8'h00;
        1: mask = 8'h0f;
        2: mask = 8'hf0;
        3: mask = 8'h55;
      endcase
      access(SOC_MEM_WRITE, p_sequencer.cfg.mem_base + i*8, next_data(), mask);
      access(SOC_MEM_READ, p_sequencer.cfg.mem_base + i*8);
    end
    p_sequencer.state.stage = SOC_DRAINING;
    wait (p_sequencer.state.pending_count == 0);
    repeat (2) @(posedge p_sequencer.cfg.observe.clk);
    p_sequencer.cfg.clk_ctrl.set_clock(0, 10ns);
    p_sequencer.state.stage = SOC_DONE;
  endtask
endclass
