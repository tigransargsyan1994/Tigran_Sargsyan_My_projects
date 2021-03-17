import random

def guesser():
    z = random.randint(1, 100)
    k = 0
    while True:
        t1 = int(input('Give me a number '))
        if t1 == z:
            print(f'Bingo! You guessed it in {k+1} guesses') ; break
        elif t1>z:
            print('Too high!')
        elif t1<z:
            print('Too low!')
        k += 1

guesser()