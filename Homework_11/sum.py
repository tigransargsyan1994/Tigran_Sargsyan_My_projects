def sum(lst):


    sum1 = 0

    for elem in lst:
        sum1 += elem

    return sum1

lst = [int(x) for x in input().split()]
result = sum(lst)

print(result)