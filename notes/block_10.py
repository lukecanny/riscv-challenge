# Block 10

MEM0Dat = []
MEM1Dat = []

# For each core
for RVCore in range(0,2):
    hostCtrl.write(0,int('1',2))        # Assert hostCtrl signal 
    host_memWr.write(0,int('0',2))      # Don't assert memory write signal

    # Select core
    bit = str(RVCore)
    host_memAdd_15 = int(bit,2)
    host_memAdd_14_13 = int('01',2) #binary # Selecting memory
    
    # Set remainder of address to 0.
    host_memAdd_12_7 = int('000000',2) #binary
    host_memAdd_6_0 = int('0000000',2) #binary
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:06b}'.format(host_memAdd_12_7) + '{0:07b}'.format(host_memAdd_6_0)
    
    
    if RVCore == 0:
        print("Memory of RVCore0\n")
    elif RVCore == 1:
        print("\nMemory of RVCore1\n")

    # Dealing with 6 down to 0 now, max 128 options. We search between 67 and 0 (0x43 to 0)
    for i in range(0,68):
        host_memAdd_6_0 = int('{0:07b}'.format(i),2)
        host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:06b}'.format(host_memAdd_12_7) + '{0:07b}'.format(host_memAdd_6_0)
        host_memAdd.write(0,int(host_memAdd_str,2))
        # Read the memory block and append to relevant core
        if RVCore == 0:
            MEM0Dat.append(hex(datToHost.read()))
        elif RVCore == 1:
            MEM1Dat.append(hex(datToHost.read()))
        if(DATA_VIEW == 1):
            if(hex(datToHost.read()) != "0x0"):
                print("Host Address:", hex(i), "\tData: ", hex(datToHost.read()))
        elif(DATA_VIEW ==0):
            print("Host Address:", hex(i), "\tData: ", hex(datToHost.read()))
        sleep(period)   # Sleep for a period between reads.

    # Reset everything and wait 10 cycles
    hostCtrl.write(0,int('0',2))
    host_memAdd_15 = int('0',2)
    host_memAdd_6_0 = int('0000000',2)
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:06b}'.format(host_memAdd_12_7) + '{0:07b}'.format(host_memAdd_6_0)
    host_memAdd.write(0,int(host_memAdd_str,2))
    sleep(10*period)
    
print("\nOperation Finished")