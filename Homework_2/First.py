import sys
n = sys.argv



if n[1].isdigit():
    print('digit')
elif n[1].isalpha():
    print('string')
elif n[1].isalnum():
    print('aplha-numeric')