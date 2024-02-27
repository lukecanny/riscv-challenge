# Block 8
hostCtrl.write(0,int('0',2))        # Deassert host control
host_memWr.write(0,int('0',2))      # Deassert memWr
for i in range(0,300):              # Step through program 300 times.
    step.write(0,int('1',2))
    sleep(period)
    step.write(0,int('0',2))
    sleep(period)
print("\nOperation Finished")