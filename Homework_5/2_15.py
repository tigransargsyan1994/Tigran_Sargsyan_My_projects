

import sys
lst = [int(k) for k in sys.argv[1:]]

def double(lst):
    dict1 = dict.fromkeys(lst)


    for key in dict1.keys():
        dict1[key] = lst.count(key)

    for k, val in dict1.items():
        if val > 1:
            return(k)

result = double(lst)
print(result)