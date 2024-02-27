# Block 2
# Load RISCV2Core Processor
rv = Overlay("RV2Core.bit")
# Define Input Signal (AXI GPIO)
rstN = rv.rstN
step = rv.step
runAll = rv.runAll
hostCtrl = rv.hostCtrl
host_memWr = rv.host_memWr
host_memAdd = rv.host_memAdd
host_datToMem = rv.host_datToMem
# Define Output Signal (AXI GPIO)
datToHost = rv.datToHost
# Define Internal Signal/Variables
period = 2e-08 #20ns
ABI_Array = ['zero','ra','sp','gp','tp','t0','t1','t2','s0/fp','s1','a0','a1','a2','a3','a4','a5','a6','a7',
             's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','t3','t4','t5','t6']
WRITE_VIEW = 1; #0 = No printing. 1 = Print everything
DATA_VIEW = 0; #0 = Print Everything. 1 = Print only Data Locations