# Block 5
WRITE_VIEW = WRITE_VIEW
for RVCore in range(0,2):
    hostCtrl.write(0,int('1',2));
    host_memWr.write(0,int('1',2)); 
    bit = str(RVCore)
    host_memAdd_15 = int(bit,2)
    host_memAdd_14_13 = int('01',2) #binary
    host_memAdd_12_6 = int('0000000',2) #binary
    host_memAdd_5_0 = int('000000',2) #binary
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    if RVCore == 0:
        print("Memory of RVCore0\n")
    elif RVCore == 1:
        print("\nMemory of RVCore1\n")
    for i in range(0,64):
        host_memAdd_5_0 = int('{0:06b}'.format(i),2)
        host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
        host_memAdd.write(0,int(host_memAdd_str,2))
        host_datToMem.write(0,0x00000000)
        if(WRITE_VIEW == 1):
            print("Host Address:", hex(i), "\tData: 0x00000000")
        sleep(period)
    
    hostCtrl.write(0,int('0',2))
    host_memWr.write(0,int('0',2))
    host_memAdd_15 = int('0',2)
    host_memAdd_14_13 = int('00',2) 
    host_memAdd_5_0 = int('000000',2) #binary
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
print("\nOperation Finished")