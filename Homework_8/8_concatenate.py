import sys
a = int(sys.argv[1])
b = int(sys.argv[2])

def concatenate(a, b):
    lst = []
    b_new = b
    while b >= 1:
        lst.append(b % 10)
        b //= 10
    #     print(len(lst))
    return(a * 10 ** (len(lst)) + b_new)


result = concatenate(a, b)
print(result)