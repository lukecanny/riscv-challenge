# Observed Memory Mapping

14:13 - 00 = Instruction Memory

14:13 - 10 = Memory

14:13 - 01 = Register Banks

# Operations

**Clear Memory Bank** - Block 5

**Write Memory Bank** - Block 6

**Write Instruction Memory** - Block 7 

**Read Memory Bank** - Block 10

**Read Instruction Memory** - Block 8

**Read Register Banks** - Block 11

# Summary of Notebook

- 0 - Import Libs
- 1 - Fill Array with Sample Data
- 2 - Create signals
- 3 - Load IM arrays
- 4 - Set inital signals of RVs
- 5 - Write 0 to all mem blocks
- 6 - Write "data" to core 1 mem block
- 7 - Write to IM
- 8 - Run instructions
- 9 - Read IM
- 10 - Read MEM
- 11 - Read RBs
- 12 - Save RB.txt, MEM.txt, IM.txt
- 13 - C Compiler?

# Raspberry Pi Cam commands 

```
./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -f 1" -o "./output_http.so -p 8080 -w ./www"
```

```
ngrok start --config=.config/ngrok/ngrok.yml
```