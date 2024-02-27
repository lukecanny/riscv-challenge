# Block 7

# For each core: 0 and 1
for RVCore in range(0,2):
    # Assert host control
    hostCtrl.write(0,int('1',2))
    # Assert memory write
    host_memWr.write(0,int('1',2))
    bit = str(RVCore) # Select appropriate core
    host_memAdd_15 = int(bit,2)
    host_memAdd_14_13 = int('00',2) #binary     ##### 14-13 IS NOW 00 - Seems to now select INSTRUCTION MEMORY
    host_memAdd_12_6 = int('0000000',2) #binary
    host_memAdd_5_0 = int('000000',2) #binary

    # Assert 0x00000000 or 0x00007000 (Core 0 and 1 respectively)
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    
    # Print title
    if RVCore == 0:
        print("Write to IM0(Instruction Memory of RVCore0)\n")
    elif RVCore == 1:
        print("\nWrite to IM1(Instruction Memory of RVCore1)\n")    
    
    # For 64 values, 
    for i in range(0,64):
        # 5 down to 0 is the address
        host_memAdd_5_0 = int('{0:06b}'.format(i),2)
        host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
        
        # Assert the memory address
        host_memAdd.write(0,int(host_memAdd_str,2))
        
        if RVCore == 0:
            host_datToMem.write(0,IM0Array[i])  # Load datToMem from  Instruction memory array
            if(WRITE_VIEW == 1):
                print("Address: ",hex(int(host_memAdd_str,2)), "\t Host Address: ", hex(i), "\tData: ",hex(IM0Array[i]))
        elif RVCore == 1:
            host_datToMem.write(0,IM1Array[i])
            if(WRITE_VIEW == 1):
                print("Address: ",hex(int(host_memAdd_str,2)), "\t Host Address: ", hex(i), "\tData: ",hex(IM1Array[i]))
        sleep(period)   # Repeat for all instructinos
    hostCtrl.write(0,int('0',2))    # once completed, assert all zeroes and wait for 10 cycles 
    host_memWr.write(0,int('0',2))
    host_memAdd_15 = int('0',2) #binary
    host_memAdd_5_0 = int('000000',2) #binary
    sleep(10*period)  
print("\nOperation Finished")