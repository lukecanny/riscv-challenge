# Block 5

# host_memAdd_31_16 was never addressed in this block - Assuming all zeros as from last block

# For each core: 0 and 1 
hostCtrl.write(0,int('1',2));       # Enable hostCtrl
host_memWr.write(0,int('1',2));     # Assert host_memWr to 1
bit = str(RVCore)                   # Bit is either 0 or 1 depending on core 
host_memAdd_15 = int(bit,2)         # Bit 15 is the core select bit.

host_memAdd_14_13 = int('01',2) #binary         01 and dont know why
host_memAdd_12_6 = int('0000000',2) #binary     12-6 is all 0
host_memAdd_5_0 = int('000000',2) #binary       5-0 is all 0

#                  (core) (???)
#      31-16         15   14-13    12-6      5-0
# 0000000000000000   0     01     0000000   000000
# 0x00002000 - Core 0
# 00000000000000001010000000000000
# 0x0000a000 - Core 1

# 3FFC - Max Value according to the memory map
# 0011 1111 1111 1100 
#   ^ bit 13.
# Notes: Write on rising clk edge, read on falling clk edge

# Format the host_memAdd, pointing at the mem data/stack
host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)

# Print if dealing with Core 0 or Core 1.
if RVCore == 0:
    print("Memory of RVCore0\n")
elif RVCore == 1:
    print("\nMemory of RVCore1\n")

# We are dealing with 64 memory spaces
for i in range(0,64):
    # Increment the bottom 6 bits between 00 and 3F (0-63) 
    host_memAdd_5_0 = int('{0:06b}'.format(i),2)
    # Reformat the string again
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    # Assert memory address on the host_memAdd
    host_memAdd.write(0,int(host_memAdd_str,2))
    # Assert datToMem as all zeroes
    host_datToMem.write(0,0x00000000)
    if(WRITE_VIEW == 1):
        print("Host Address:", hex(i), "\tData: 0x00000000")
    sleep(period)

# Once completed, deassert hostCtlr, host_memWr, and zero out the memAdd again
hostCtrl.write(0,int('0',2))
host_memWr.write(0,int('0',2))
host_memAdd_15 = int('0',2)         # <= Clearing the core option
host_memAdd_14_13 = int('00',2)     # <= Clearing the 14/13 bit ??
host_memAdd_5_0 = int('000000',2) #binary
host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
print("\nOperation Finished")