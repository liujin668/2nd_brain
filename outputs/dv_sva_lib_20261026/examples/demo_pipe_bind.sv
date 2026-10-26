// Bind every demo_pipe instance. Parameters resolve in the target scope.
bind demo_pipe dv_sva_ready_valid #(.DATA_WIDTH(DATA_WIDTH))
  u_output_protocol_sva (
    .clk(clk), .rst_n(rst_n), .valid_i(out_valid),
    .ready_i(out_ready), .data_i(out_data)
  );
