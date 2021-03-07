from sys import exit

def remove_number(lst):

    if k in lst:
        z = lst.index(k)

        for i in range(len(lst) - z - 1):
            lst[z], lst[z+1] = lst[z+1], lst[z]
            z += 1

        lst[-1] = 0

        return lst
    else:
        return 'Number does not exist in sequence'


try:
    lst = [int(x) for x in input('Input 10 numbers').split()]
    if len(lst) != 10:
        print('Sequence lenght must be 10')
        exit()
except ValueError:
    print('Input integers please')

try:
    k = int(input('k = '))
except ValueError:
    print('K must be integer')
else:
    result = remove_number(lst)
    print(result)
#

