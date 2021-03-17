def number_guesser(count, start, end):

    # if count > 7:
    #     return 'I couldn’t guess in 10 steps! This means you cheated!'

    mid = (start + end) // 2
    print('My guess number :', mid)

    userinput = int(input())
    if userinput == -1:     #it means computer should guess a smaller number
        return number_guesser(count + 1, start, mid)

    elif userinput == 0:
        return f'I guessed in {count} steps!'

    elif userinput == 1:      #it means computer should guess a bigger number
        return number_guesser(count + 1, mid, end)

result = number_guesser(1, 0, 100)
print(result)