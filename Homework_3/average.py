import sys

list_of_numbers = sys.argv

del list_of_numbers[0]

integers = [int(k) for k in list_of_numbers]

average = sum(integers) / len(integers)
print(average)