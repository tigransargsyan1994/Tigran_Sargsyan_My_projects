def bubble_sort_ascending(nums):
    n = len(nums)
    for i in range(n):
        is_swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True
        if  not is_swapped:
            break
    return nums

def bubble_sort_descending(nums):
    n = len(nums)
    for i in range(n):
        is_swapped = False
        for j in range(n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swapped = True
        if  not is_swapped:
            break
    return nums



nums = [int(elem) for elem in input('input numbers').split()]

print(bubble_sort_ascending(nums))

print(bubble_sort_descending(nums))
