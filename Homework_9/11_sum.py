import sys
n = int(sys.argv[1])


def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10

    return sum

result = sum_of_digits(n)
print(result)