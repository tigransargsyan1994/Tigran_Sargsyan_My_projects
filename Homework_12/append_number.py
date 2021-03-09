def append_number(lst, k, m):
    lst.append(k)

    i = -1
    while lst[m - 1] != k:
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        i -= 1

    return lst

try:
    lst = [int(x) for x in input('Input numbers').split()]
    k = int(input('number k = '))
    m = int(input('m-th position  = '))

except ValueError:
    print('only integers please')
else:
    result = append_number(lst, k, m)
    print(result)
