class soc_tl_monitor extends uvm_component;
  `uvm_component_utils(soc_tl_monitor)
  soc_run_state state;
  uvm_analysis_imp #(soc_mem_rsp, soc_tl_monitor) raw_export;
  uvm_analysis_port #(soc_mem_rsp) observed_ap;
  function new(string name, uvm_component parent);
    super.new(name, parent);
    raw_export = new("raw_export", this);
    observed_ap = new("observed_ap", this);
  endfunction
  // A transaction TAP, not a pin-level protocol monitor. A real VIP adapter
  // replaces this input with decoded, accepted/completed interface events.
  function void write(soc_mem_rsp response);
    soc_mem_rsp snapshot;
    if (response == null) begin
      state.fail("NULL_OBSERVATION", "Backend supplied a null observation");
      return;
    end
    if (!$cast(snapshot, response.clone()))
      `uvm_fatal("OBSERVATION_CLONE", "Cannot clone response")
    state.observed_count++;
    observed_ap.write(snapshot);
  endfunction
endclass
