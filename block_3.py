

IM0Array = []; IM1Array = [] # Array Declaration
RVCore = 0 # or 1.

string = ''; list = []; fullString = ''; data = []; strArray = ''; row = 0
instrArray = []


# Depending on the core we are dealing with:
#   Load the relevant code
if RVCore == 0:
    file = open("swapX3DigitX4WithX5DigitX6_MachineCode.txt")
    string = file.read(); file.close
    instruction = string.split('\n')
elif RVCore == 1:
    file = open("RV2Core1_MachineCode.txt")
    string = file.read(); file.close
    instruction = string.split('\n')


# Check each line of machine code, if 0x isn't in front. add it
for i in range(0,len(instruction)):
    if (len(instruction[i]) == 10):
        fullString = fullString + instruction[i] + '\n'
    elif(len(instruction[i]) == 8):
        fullString = fullString + "0x" + instruction[i] + '\n'




# For the remainder of the instruction memory, add 0x00000000
for i in range(0,(64-len(instruction))):
        fullString = fullString + '0x00000000' + '\n'

# Data is now equal to the full 64 lines (64 * 4 bytes = 256 byte IM)
data = fullString.split('\n')
for indx in range(0,len(data)-1):   # 64 cycles always
    if indx == 63:  # If last line, we dont add ,
        strArray = strArray + data[indx]
    else:           # Add 
        strArray = strArray + data[indx] + ", "
    row = row + 1
    if row == 8:
        if indx == 63:
            strArray = strArray
        else:
            strArray = strArray + "\n"
        row = 0 

# The above loop forms the following as a big string:
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,    
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
# 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007 <= this is 63, so we dont add comma or new line

if(WRITE_VIEW == 1):
    IMArrayStr = 'IM' + str(RVCore) + 'Array = [' + strArray + ']'
    print(IMArrayStr, '\n')
        
# Then finally it all gets stored as 
# instrArray = [
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,    
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007,
    # 0x00000000, 0x00000001, 0x00000002, 0x00000003, 0x00000004, 0x00000005, 0x00000006, 0x00000007
# ]
instrArray = strArray.split(", ")
for i in instrArray:
    if RVCore == 0:
        IM0Array.append(int(i,16))
    elif RVCore == 1:
        IM1Array.append(int(i,16))
