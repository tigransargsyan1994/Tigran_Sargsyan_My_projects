import sys

a = int(sys.argv[1])
b = int(sys.argv[2])


def divisor(x, y):
    minimum = min(x, y)
    for num in range(minimum, 0, -1):
        if x % num == 0 and y % num == 0:
            return num


result = divisor(a, b)
print(result)
