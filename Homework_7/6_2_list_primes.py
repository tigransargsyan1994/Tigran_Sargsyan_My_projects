import sys

a = sys.argv[1]
b = sys.argv[2]

def list_of_primes(start, stop):
    all1 = set()
    for num in range(start, stop+1):
        all1.add(num)

    non_primes = set()

    for n in range(start, (stop // 2 + 1)):
        variable = 2
        while n * variable <= stop:
            non_primes.add(n*variable)
            variable += 1
    primes = all1 - non_primes
    return primes

result = list_of_primes(int(a), int(b))
print(result)