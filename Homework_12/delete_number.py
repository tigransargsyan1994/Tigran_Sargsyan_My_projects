def delete_number(lst, m):

        for i in range(len(lst) - m - 1):
            lst[m], lst[m+1] = lst[m+1], lst[m]
            m += 1

        del lst[-1]

        return lst

try:
    lst = [int(x) for x in input('Input numbers').split()]
    m = int(input('m = '))

except ValueError:
    print('only integers please')
else:
    result = delete_number(lst, m-1)
    print(result)
