import sys

list_of_names = sys.argv

del list_of_names[0]

print(max(list_of_names, key=len))