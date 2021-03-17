import sys

list_of_numbers = sys.argv

del list_of_numbers[0]

integers = [int(k) for k in list_of_numbers]


for elem in integers:
    if integers.count(elem) > 1:
        print(elem)
        break

