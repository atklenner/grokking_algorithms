def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low < high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == target:
            return True
        if guess < target:
            low = mid
        else:
            high = mid
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))