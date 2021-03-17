import sys

s = sys.argv[1]

def palindrom_recursion(s):
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        if s[0] == s[-1]:
            return palindrom_recursion(s[1:-1])
        else:
            return False

if palindrom_recursion(s):
    print('This string is a palindrom')
else:
    print('This is not a palindrom')