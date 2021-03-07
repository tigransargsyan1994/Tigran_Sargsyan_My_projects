def make_reverse(lst):


    lst.reverse()

    return (lst)

lst = [int(x) for x in input().split()]
result = make_reverse(lst)
print(result)