def set_1(lst):
    new_list = set(lst)
    return new_list


lst = [int(x) for x in input('Input numbers').split()]
result = set_1(lst)

print(result)
