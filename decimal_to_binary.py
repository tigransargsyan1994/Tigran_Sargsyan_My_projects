def decimal_to_binary(num):
    if num > 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


number = 8

decimal_to_binary(number)