import sys

a = sys.argv[1]

def reverse(n):
    lst = []

    while n >= 1:
        mnacord = n % 10
        lst.append(mnacord)
        n = n // 10

    rvrsd = 0
    z = 0
    power = len(lst) - 1
    for num in range(len(lst)):
        rvrsd += lst[z] * 10 ** power
        z += 1
        power -= 1

    return rvrsd

result = reverse(int(a))
print(result)