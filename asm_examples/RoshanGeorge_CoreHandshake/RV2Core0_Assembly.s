# Names: 				Roshan George, Fearghal Morgan
# Date: 				01/May/2021
#
# Description:			The source assembly program for RVCore0.
#
# Dictionary:
#
#	op0 = 0(0x100)  	data to core1
#	op1 = 4(0x100)  	rq bit to core1
#	in0 = 8(0x100)  	data from core1
#	in1 = 12(0x100) 	ack bit from core0
#
#	sendAddRq1  	 	Transfer core1 memory address to core1 on outport0. Assert rq on outport1(0) to validate outport0.
#   pollUntilAck1    	Poll until core1 ack asserted (inport1(0)=1), validating data received on inport0.
#   getDat	  			Read inport0 data (= addressed core1 memory data).
#   sendRq0	  			Deassert rq on outport1(0) to core1, handshaking data received.
#   pollUntilAck0		Poll until inport1(0)=0, indicating completion of add/data transfer sequence. 
#   datProc	  			Process data received from core1.


addi a0, zero, 256		# Base Address
addi a1, zero, 1		# Ack1 Bit
addi a2, zero, 0		# Data (Core1 Memory) Address

main:
	call sendAddRq1
	addi a3, a3, 1
	call pollUntilAck1
	addi a3, a3, 1
	call getDat
	addi a3, a3, 1
	call sendRq0
	addi a3, a3, 1
	call pollUntilAck0
	addi a3, a3, 1
	call datProc
	addi a3, a3, 1
	end: jal zero, end
	
sendAddRq1:
	sw a2, 0(a0)			 
	sw a1, 4(a0)
		
pollUntilAck1:
	lw t0, 12(a0)		 
	beq t0, zero, pollUntilAck1
			
getDat:
	lw t2, 8(a0)		
		
sendRq0:
	sw zero, 4(a0)
		
pollUntilAck0:
	lw t0, 12(a0)		
	bgt t0, zero, pollUntilAck0	
		
datProc:
	addi t6, t2, 0xFF	 


