#include "soc_platform.h"

/* Caller supplies a RESERVED scratch region, outside image/stack/result/DT.
 * This is a test algorithm, not startup code and not a CPU boot proof.
 * Cacheability and visibility are a platform capability contract. */
int soc_memory_smoke(uint64_t scratch_base, size_t scratch_size)
{
    static const uint32_t patterns[] = {
        UINT32_C(0x00000000), UINT32_C(0xffffffff),
        UINT32_C(0x55aa55aa), UINT32_C(0xaa55aa55)
    };
    size_t i;
    uint32_t observed;
    if ((scratch_base & UINT64_C(3)) != 0 || scratch_size < 4)
        return 10;
    for (i = 0; i < sizeof(patterns) / sizeof(patterns[0]); ++i) {
        if (soc_mmio_write32(scratch_base, patterns[i]) != SOC_OK)
            return 20;
        if (soc_memory_barrier() != SOC_OK)
            return 21;
        if (soc_mmio_read32(scratch_base, &observed) != SOC_OK)
            return 22;
        if (observed != patterns[i])
            return 30;
    }
    return 0;
}
