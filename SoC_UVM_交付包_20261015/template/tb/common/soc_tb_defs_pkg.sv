package soc_tb_defs_pkg;
  timeunit 1ps;
  timeprecision 1ps;

  // Testbench types, not a description of the final SoC address map.
  typedef logic [63:0] soc_addr_t;
  typedef logic [63:0] soc_data_t;
  typedef enum logic {SOC_MEM_READ, SOC_MEM_WRITE} soc_mem_op_e;
  typedef enum int {SOC_INIT, SOC_RESET, SOC_READY, SOC_RUNNING,
                    SOC_DRAINING, SOC_DONE} soc_stage_e;

  localparam int SOC_RESULT_SCHEMA_VERSION = 1;
  // Deliberately above 4 GiB to exercise the template's address representation.
  localparam soc_addr_t SELFTEST_MEM_BASE = 64'h0000_0001_0000_1000;
  localparam int unsigned SELFTEST_MEM_BYTES = 4096;
endpackage
