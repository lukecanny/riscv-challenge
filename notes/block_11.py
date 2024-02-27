# Block 11

RB0Dat = []
RB1Dat = []

# For each core
for RVCore in range(0,2):
    hostCtrl.write(0,int('1',2))        # Assert host control
    host_memWr.write(0,int('0',2))      # assert memory write
    
    bit = str(RVCore)                   # Select Core      
    host_memAdd_15 = int(bit,2)
    
    host_memAdd_14_13 = int('10',2)     # 10 for Register Bank

    host_memAdd_12_5 = int('00000000',2) #binary
    host_memAdd_4_0 = int('00000',2) #binary
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:08b}'.format(host_memAdd_12_5) + '{0:05b}'.format(host_memAdd_4_0)
    if RVCore == 0:
        print("Register Bank of RVCore0\n")
    elif RVCore == 1:
        print("\nRegister Bank of RVCore1\n")
    for i in range(0,32):
        host_memAdd_4_0 = int('{0:05b}'.format(i),2)
        host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:08b}'.format(host_memAdd_12_5) + '{0:05b}'.format(host_memAdd_4_0)
        host_memAdd.write(0,int(host_memAdd_str,2)) 
        if RVCore == 0:
            RB0Dat.append(hex(datToHost.read()))
        elif RVCore == 1:
            RB1Dat.append(hex(datToHost.read()))
        regBankStr = "X"+"{:02d}".format(i)
        if(DATA_VIEW == 1):
            if(hex(datToHost.read()) != "0x0"):
                print(regBankStr, '  ', ABI_Array[i], '\tData: ',hex(datToHost.read()))
        elif(DATA_VIEW== 0):
            print(regBankStr, '  ', ABI_Array[i], '\tData: ',hex(datToHost.read()))
        sleep(period)
    hostCtrl.write(0,int('0',2))
    host_memAdd_15 = int('0',2)
    host_memAdd_4_0 = int('00000',2)
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:08b}'.format(host_memAdd_12_5) + '{0:05b}'.format(host_memAdd_4_0)
    host_memAdd.write(0,int(host_memAdd_str,2))
    sleep(10*period)
    
print("\nOperation Finished")    