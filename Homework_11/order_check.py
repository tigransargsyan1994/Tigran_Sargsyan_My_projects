def check_ordered(lst):
    if lst[0] < lst[1]:
        for k in range(len(lst)-1):
            if lst[k] < lst[k+1]:
                continue
            else:
                return False
        return 'Ascending order'
    else:
        for k in range(len(lst)-1):
            if lst[k] > lst[k+1]:
                continue
            else:
                return False
        return 'Descending order'

if __name__ == '__main__':
    result1 = check_ordered([1,4,7,9])
    result2 = check_ordered([100, 49, 17, 9])
    result3 = check_ordered([1, 47, 17, 79])
    print(result1)
    print(result2)
    print(result3)