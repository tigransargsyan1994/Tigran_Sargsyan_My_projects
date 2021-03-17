import sys

list_of_numbers = sys.argv

del list_of_numbers[0]

integers = [int(k) for k in list_of_numbers]

maximum = (max(integers))

index = (integers.index(max(integers)))

print(f'index : {index}, max : {maximum}')