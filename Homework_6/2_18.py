import sys

x = sys.argv[1]
y = sys.argv[2:]
print(x)
print(y)

def istrue(a, b):
    if a in b:
        return True
    return False

result = istrue(x, y)
print(result)