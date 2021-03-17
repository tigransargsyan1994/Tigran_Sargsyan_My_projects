import sys

s = sys.argv
s = s[1:]


def bin(a, b, k):
    if k == '&':
        return a & b
    elif k == '|':
        return a | b
    else:
        return a ^ b

result = bin(int(s[0]),int(s[1]),s[2])
print(result)