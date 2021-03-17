import sys

z = sys.argv
num = int(z[1])

if num in range(1, 11):

    dictionary = {1: 'one',
                  2: 'two',
                  3: 'three',
                  4: 'four',
                  5: 'five',
                  6: 'six',
                  7: 'seven',
                  8: 'eight',
                  9: 'nine',
                  10: 'ten'}
    print(dictionary[num])

else:
    print('Wrong input')