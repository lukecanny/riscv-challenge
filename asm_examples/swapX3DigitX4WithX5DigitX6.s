# RISC-V assembly program
# swapX3DigitX4WithX5DigitX6
# Anthony Bird, Luke Canny Oct 2022
#
# Registers:
#	x3, x5 			= 	source registers
#	x4, x6 			= 	specifies digit position to swap for x3 & x5 respectively
#	x7, x9 			= 	mask for x3 & x5 respectively
# 	x8, x10, x12 	= 	counters
#	x11 			= 	holds difference between x4 & x6 values


main:
 jal  x1, setup				# Set up initial registers before program begins
 jal x1, extract_value_one	# Extract nibble from the first value given (stored in x3)
 jal x1, extract_value_two	# Extract nibble from the second value given (stored in x5)
 jal x1, swap				# Swap the two nibbles
 stall_loop:                # Stall the program forever
  nop
  j stall_loop

extract_value_one:
 addi x7,x0, 0xf			
 addi x8, x0, 0   			
 beq x8, x4, skip1			# If the position selected is zero, skip logical shift loop.
 shiftLoop1:				
  slli x7, x7, 4
  addi x8,x8,1	  			# Increment counter
  bne x8, x4, shiftLoop1	# If x8 (the counter) does not equal x4 (the desired position), loop again
 skip1:						
 and x7, x7, x3				# mask x3 to x7
 xor x3, x7, x3				# set selected nibble to 0x0 in x3. 
 jalr x0, 0(x1)				

extract_value_two:
 addi x9,x0, 0xf			
 addi x10, x0, 0   			
 beq x10, x6, skip2			
 shiftLoop2:				
  slli x9, x9, 4  			
  addi x10,x10,1			
  bne x10, x6, shiftLoop2	
 skip2:						
 and x9, x9, x5				# mask x9 to x5
 xor x5, x9, x5				# set selected nibble to 0x0 in x5. 
 jalr x0, 0(x1)				
 
swap:
 beq x4, x6, equalSwap 		# if x4 = x6
 blt x4, x6, lessThanSwap 	# if x4 < x6
 bge x4, x6, greaterThanSwap# if x4 > x6
 
equalSwap:					
 or x3, x3, x9				# insert value in x9 into x3
 or x5, x5, x7				# insert value in x7 into x5
 jalr x0, 0(x1)				
 
lessThanSwap: 
 sub x11, x6, x4			# Subtract to get difference between two positions.
 
 # swapping x9 into x3
 addi x12, x0, 0   			
 shiftLoop3:				
  srli x9, x9, 4  			
  addi x12,x12,1	  		
  bne x12, x11, shiftLoop3	
 or x3, x3, x9				
 
 # swapping x7 into x5
 addi x12, x0, 0   			
 shiftLoop4:				
  slli x7, x7, 4  			
  addi x12,x12,1	  		
  bne x12, x11 shiftLoop4	
 or x5,x5,x7				
 jalr x0, 0(x1)				
 
greaterThanSwap: 
 sub x11, x4, x6	
 
 # swapping x9 into x3 
 addi x12, x0, 0   			
 shiftLoop5:				
  slli x9, x9, 4  			
  addi x12,x12,1	  		
  bne x12, x11, shiftLoop5	
 or x3, x3, x9				
 
 # swapping x7 into x5
 addi x12, x0, 0   			
 shiftLoop6:				
  srli x7, x7, 4  			
  addi x12,x12,1	  		
  bne x12, x11, shiftLoop6	
 or x5,x5,x7				
 jalr x0, 0(x1)				
 
 
setup:
 lui x3, 0xb1ade			# x3 = b1ade000
 addi x4, x0, 7				# Selecting position 7 nibble
 lui x5, 0xb01df
 addi x5, x5, 0xce			# x5 = 0xb01df0ce
 addi x6, x0, 0				# Selecting position 0 nibble
 
 jalr x0, 0(x1)   