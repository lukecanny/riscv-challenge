# Names: 				Roshan George, Fearghal Morgan
# Date: 				01/May/2021
#
# Description:			The source assembly program for RVCore0.
#
# Dictionary:
#
#	op0 = 0(0x100)  	data to core0
#	op1 = 4(0x100)  	rq bit to core0
#	in0 = 8(0x100)  	data from core0
#	in1 = 12(0x100) 	ack bit from core1

#   pollUntilAck1    	Poll until core0 ack asserted (inport1=1), validating data received on inport0.
#   getDat	  		    Read inport0 data (= addressed core1 memory data).
#   sendAck1	  		Assert ack on outport1 to validate outport0.
#   sendDat				Transfer core1 data to core0 on outport0
#   pollUntilRq0		Poll until inport1(0)=0, indicating completion of add/data transfer sequence. 
#   sendAcq0	  		Deassert ack on outport1 to core0, handshaking data received.

addi a0, zero, 256		# Base Address
addi a1, zero, 1		# Ack1 Bit

main:
	call pollUntilAck1
	call getDat
	call sendDat
	call sendAck1
	call pollUntilRq0
	call sendAck0
	end: jal zero, end	

pollUntilAck1:
	lw t0, 12(a0)			
	beq t0, zero, pollUntilAck1	
	
getDat:
	lw t2, 8(a0)		
		
sendDat:
	lw t2, 0(t2)			
	sw t2, 0(a0)	
		
sendAck1:
	sw a1, 4(a0)			
			
pollUntilRq0:
	lw t0, 12(a0)
	bgt t0, zero, pollRq0	
		
sendAck0:
	sw zero, 4(a0)			
	addi x26, x26, 0x1
		
