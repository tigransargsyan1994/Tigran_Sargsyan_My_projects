import sys

a = sys.argv[1]

def summa(y):
    sum0 = 0
    while y >= 1:
        mnacord = y % 10
        sum0 += mnacord
        y = y // 10
    return sum0

result = summa(int(a))
print(result)