def binary_to_decimal(n):
    list1 = []
    number = n
    while number > 0:
        list1.append(number % 10)
        number //= 10
    output = 0
    k = 0
    for i in range(len(list1)):
        z = (list1[i]) * 2 ** k
        output += z
        k += 1

    return output

result = binary_to_decimal(10101)
print(result)