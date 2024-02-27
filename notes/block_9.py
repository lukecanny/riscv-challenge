# Block 9

IM0Dat = []
IM1Dat = []

# For each core:
for RVCore in range(0,2):
    # Host control asserted, memory write NOT asserted
    hostCtrl.write(0,int('1',2))
    host_memWr.write(0,int('0',2))

    # Select core bit
    bit = str(RVCore)
    host_memAdd_15 = int(bit,2)
    
    # 14/13 set to 00 (Instruction Memory)
    host_memAdd_14_13 = int('00',2) #binary
    
    # Rest of addr set to 0.
    host_memAdd_12_6 = int('0000000',2) #binary
    host_memAdd_5_0 = int('000000',2) #binary
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    
    # 0x00000000 0x00007000
    
    if RVCore == 0:
        print("Instruction Memory of RVCore0\n")
    elif RVCore == 1:
        print("\nInstruction Memory of RVCore1\n")
    
    
    
    # For all 64 addresses
    for i in range(0,64):
        # Set bottom 6 bits to 0-63 (note 2^6 = 64)
        host_memAdd_5_0 = int('{0:06b}'.format(i),2)
        host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
        # format memadd and assert on bus
        host_memAdd.write(0,int(host_memAdd_str,2))
        if RVCore == 0:
            IM0Dat.append(hex(datToHost.read()))    # For each line address, read the instructions
        elif RVCore == 1:                           # Depending on core selected, store in different arrays
            IM1Dat.append(hex(datToHost.read()))
        if(DATA_VIEW == 1):     # If verbose mode set, print to console
            if(hex(datToHost.read()) != "0x0"):     
                print("Host Address:", hex(i), "\tData: ", hex(datToHost.read()))
        elif(DATA_VIEW == 0):
            print("Host Address:", hex(i), "\tData: ", hex(datToHost.read()))
        sleep(period)   # Sleep for period between reads
    hostCtrl.write(0,int('0',2))    # reset all signals and wait for 10 periods
    host_memAdd_15 = int('0',2) 
    host_memAdd_5_0 = int('000000',2) 
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    host_memAdd.write(0,int(host_memAdd_str,2))
    sleep(10*period)
    
print("\nOperation Finished")