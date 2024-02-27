# Make a script that does the main processes of the jupyter notebook

# Not all of these libraries are needed.
from pynq import Overlay
from time import sleep
from pynq.overlays.base import BaseOverlay
from pynq.lib import Pmod_ADC
import matplotlib.pyplot as plt
import struct

class RISCV_App():

    def __init__(self, project_name="RV2Core"):
        bitstream = project_name + ".bit"
        self.rv = Overlay(bitstream)

        # Define Input Signal (AXI GPIO)
        self.rstN = self.rv.rstN
        self.step = self.rv.step
        self.runAll = self.rv.runAll
        self.hostCtrl = self.rv.hostCtrl
        self.host_memWr = self.rv.host_memWr
        self.host_memAdd = self.rv.host_memAdd
        self.host_datToMem = self.rv.host_datToMem
        # Define Output Signal (AXI GPIO)
        self.datToHost = self.rv.datToHost
        # Define Internal Signal/Variables
        self.period = 2e-08 #20ns
        self.ABI_Array = ['zero','ra','sp','gp','tp','t0','t1','t2','s0/fp','s1','a0','a1','a2','a3','a4','a5','a6','a7',
                    's2','s3','s4','s5','s6','s7','s8','s9','s10','s11','t3','t4','t5','t6']
        self.WRITE_VIEW = 1; #0 = No printing. 1 = Print everything
        self.DATA_VIEW = 0; #0 = Print Everything. 1 = Print only Data Locations

    def read_core_0_memory(self):
        pass

    def read_core_1_memory(self):
        pass

    def read_core_0_registers(self):
        pass

    def read_core_1_registers(self):
        pass

    def read_core_0_instruction_mem(self):
        pass

    def read_core_1_instruction_mem(self):
        pass

    def write_core_0_instruction_mem(self, im=None,filename=None):
        pass

    def write_core_1_instruction_mem(self, im=None,filename=None):
        pass

    def run_clock_cycle(self, number=1):
        pass
