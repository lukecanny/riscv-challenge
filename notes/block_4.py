# Block 4 Analysis

### In the previous block, the Instruction Arrays are created
# IM0Array = [
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,    
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007
# ]

# Initialising all input signals
step.write(0,int('0',2));           # Step = 0
runAll.write(0,int('0',2))          # runAll = 0
hostCtrl.write(0,int('0',2))        # hostCtrl = 0
host_memWr.write(0,int('0',2))      # host_memWr = 0

# Create host_memAdd (32 bits line, originally all set to 0)
host_memAdd_31_16 = int('0000000000000000',2)
host_memAdd_15 = int('0',2) #binary
host_memAdd_14_13 = int('00',2) #binary
host_memAdd_12_6 = int('0000000',2) #binary
host_memAdd_5_0 = int('000000',2) #binary

# host_memAdd is then set to all zeros.
host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
host_memAdd.write(0,int(host_memAdd_str,2))
# host data to mem is set to all zeroes
host_datToMem.write(0,0x00000000)

# Reset is asserted for a period.

# Assert and Deassert ResetN.
rstN.write(0,int('0',2))
sleep(1.2*period)   # Period was defined as 20ns earlier.
rstN.write(0,int('1',2))
sleep(1.2*period)
print("\nOperation Finished")