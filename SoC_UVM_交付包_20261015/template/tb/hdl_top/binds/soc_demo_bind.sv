// The only fixed hierarchy reference for this checker lives here.
// Real DUT binds belong in a profile-specific filelist.
bind soc_demo_wrapper soc_pin_checks u_soc_pin_checks(
  .clk(clk), .rst_n(rst_n), .cycle_marker(cycle_marker),
  .status($root.soc_hdl_top.assert_status)
);
