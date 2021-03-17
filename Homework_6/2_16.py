import sys

lst111 = sys.argv[1:]

def count(lst):
    str1 = ''.join(lst)
    str1 = str1.lower()

    lst1 = [elem for elem in str1]

    dict1 = dict.fromkeys(lst1)

    for key in dict1.keys():
        dict1[key] = lst1.count(key)
    returnstr = ''
    for k, v in dict1.items():
        returnstr += (str(k) + ' - ' + str(v) + '\n')
    return returnstr


result = count(lst111)
print(result)