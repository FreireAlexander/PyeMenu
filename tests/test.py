import pyemenu
import os
from readchar import key, readkey

a = ''
while True:
    a += readkey()
    clear()
    print(a)

