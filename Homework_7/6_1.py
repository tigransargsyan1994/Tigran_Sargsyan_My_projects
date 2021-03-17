import sys

a = sys.argv[1]

def is_prime(n):
    for k in range(2, n // (2 + 1)):
        if n % k == 0:
            return False
    return True

if is_prime(int(a)):
    print(f'{a} is Prime')
else:
    print(f'{a} is not Prime')


