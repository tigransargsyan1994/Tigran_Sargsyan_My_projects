import sys
n = int(sys.argv[1])

def power(n):
    lst1 = []
    k = 1
    while 2 ** k <= n:
        lst1.append(2 ** k)
        k += 1

    if n in lst1:
        return'Number is power of 2'
    else:
        return'Not a power of 2'


result = power(n)
print(result)