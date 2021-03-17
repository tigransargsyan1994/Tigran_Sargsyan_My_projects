import sys

list_of_numbers = sys.argv

del list_of_numbers[0]

integers = [int(k) for k in list_of_numbers]

last = integers[-1]
summa = int((last * (last + 1)) / 2)
print(summa)