import sys
n = int(sys.argv[1])


def palindrom(n):
    number = n
    lastlist = []
    while n >= 1:
        lastnum = n % 10
        lastlist.append(lastnum)
        n = n // 10

    reverse = 0
    k = len(lastlist) - 1
    for i in range(len(lastlist)):
        reverse += lastlist[i] * 10 ** k
        k -= 1

    if number == reverse:
        return 'Number is Palindrome'
    else:
        return 'Number is not Palindrome'


result = palindrom(n)
print(result)