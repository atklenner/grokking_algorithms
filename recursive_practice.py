def sum(num_array):
    if len(num_array) == 0:
        return 0
    else:
        return num_array[-1] + sum(num_array[0:-1])

print(sum([2,4,6]))
print(sum(list(range(101))))

def count(list):
    if len(list) == 1:
        return 1
    else:
        return 1 + count(list[0:-1])

print(count([2,4,6]))
print(count(list(range(100))))

def max_value(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[-1] if list[-1] > max_value(list[0:-1]) else max_value(list[0:-1])

print(max_value([1,2,3,99,5]))

def binary_search_recursive(list, target):
    mid_index = (len(list) - 1) // 2
    guess = list[mid_index]
    if len(list) == 1:
        if list[0] == target:
            return True
        else:
            return None
    else:
        if guess < target:
            return binary_search_recursive(list[mid_index:], target)
        elif guess > target:
            return binary_search_recursive(list[:mid_index + 1], target)
        else:
            return True

print(binary_search_recursive([1,2,3,4,5], 2))