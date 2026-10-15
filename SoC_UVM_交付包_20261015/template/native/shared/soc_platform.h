#ifndef SOC_PLATFORM_H
#define SOC_PLATFORM_H

#include <stddef.h>
#include <stdint.h>

/* Platform contract, not a working N2 BSP. Implement one backend per build. */
typedef enum {
    SOC_OK = 0,
    SOC_BUS_ERROR = 1,
    SOC_TIMEOUT = 2,
    SOC_UNSUPPORTED = 3,
    SOC_INVALID_ARGUMENT = 4
} soc_status_t;

typedef enum {
    SOC_SW_RUNNING = 1,
    SOC_SW_PASS = 2,
    SOC_SW_FAIL = 3
} soc_sw_state_t;

#define SOC_RESULT_MAGIC UINT32_C(0x534F4352)
#define SOC_RESULT_VERSION UINT32_C(1)

/* Logical wire fields. Serialize explicitly in little endian; do not dump a
 * compiler-dependent native struct into memory. The agreed wire size is 40B:
 * magic@0, version@4, run_token@8, test_id@16, state@20, error_code@24,
 * reserved@28, heartbeat@32. */
typedef struct {
    uint64_t run_token;
    uint32_t test_id;
    soc_sw_state_t state;
    uint32_t error_code;
    uint64_t heartbeat;
} soc_sw_result_t;

soc_status_t soc_mmio_read32(uint64_t address, uint32_t *value);
soc_status_t soc_mmio_write32(uint64_t address, uint32_t value);
soc_status_t soc_wait_ns(uint64_t delay_ns);
soc_status_t soc_memory_barrier(void);
soc_status_t soc_cache_clean(uint64_t address, size_t length);
soc_status_t soc_cache_invalidate(uint64_t address, size_t length);
/* Publication contract: initialize a fresh token/RUNNING state before use.
 * Publish final payload first, ensure payload visibility, then commit state
 * LAST using a platform-confirmed atomic aligned 32-bit write. Ensure commit
 * visibility too. Cache clean/order requirements belong to the backend.
 * Reader must validate token/version and a stable commit before accepting.
 * Return non-OK if these guarantees cannot be provided. */
soc_status_t soc_publish_result(const soc_sw_result_t *result);
void soc_log(const char *message);

/* Backend must preserve 64-bit addresses through C/DPI/SV/VIP.
 * Read output is valid ONLY when SOC_OK is returned. Timeout/error is never
 * converted to zero data. CPU-only operations in host DPI must be UNSUPPORTED
 * unless the stated test semantics truly require no CPU-side operation. */
#endif

