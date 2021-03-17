from sys import argv
import subprocess

a = argv[1]
b = (argv[2:])
print(a)
print(b)

c = ' '.join(b)
print(c)
# e = d[1:-1]
# print(e)
d = c[1:-1]
print(d)
