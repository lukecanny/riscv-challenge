# Targetting only Core 1.


RVCore = 1                      
hostCtrl.write(0,int('1',2))    # Assert hostCtrl
host_memWr.write(0,int('1',2))  # Assert memWr
bit = str(RVCore)               # 15 is high for core 1.
host_memAdd_15 = int(bit,2)     
host_memAdd_14_13 = int('01',2) # We are setting 14/13 back to 01 for whatever reason
host_memAdd_12_6 = int('0000000',2)     # Zeroing out the rest of the address bits
host_memAdd_5_0 = int('000000',2) 
# Format string and put in on the bus
host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
host_memAdd.write(0,int(host_memAdd_str,2))

if RVCore == 0: # Ignore
    print("Memory of RVCore0\n")
elif RVCore == 1: # Print title
    print("\nMemory of RVCore1\n")

for i in range(0,32): # Running 32 times
    # Format 5:0 to 0-32
    host_memAdd_5_0 = int('{0:06b}'.format(i),2)
    host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
    # Assert memAdd on the bus
    host_memAdd.write(0,int(host_memAdd_str,2))
    data = wave[i];
    # datToMem set to value in the wave array (this wouldve been a sine way before)
    host_datToMem.write(0,data)
    # Print address and value to be placed in memory
    if(WRITE_VIEW == 1):
        print("Host Address: ", hex(i),"\tData: ", hex(data));
    sleep(period)   # Sleep for a period and then move to next value

# Reset everything back to 0 before closing up again
host_memAdd_15 = int('0',2) #binary
host_memAdd_14_13 = int('00',2) #binary
host_memAdd_5_0 = int('000000',2) #binary
host_memAdd_str = '{0:016b}'.format(host_memAdd_31_16) + '{0:01b}'.format(host_memAdd_15) + '{0:02b}'.format(host_memAdd_14_13) + '{0:07b}'.format(host_memAdd_12_6) + '{0:06b}'.format(host_memAdd_5_0)
host_memAdd.write(0,int(host_memAdd_str,2))

# Wait for 10 more periods before quitting.
sleep(10*period)    
print("\nOperation Finished")