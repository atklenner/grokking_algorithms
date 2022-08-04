def selection_sort(unsorted_list):
    sorted_list = []
    for i in range(len(unsorted_list)):
        smallest_index = find_smallest_index(unsorted_list)
        sorted_list.append(unsorted_list.pop(smallest_index))
    return sorted_list

def find_smallest_index(list):
    min = list[0]
    min_index = 0
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            min_index = i
    return min_index

def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target:
            return True
        if mid < target:
            low = mid
        else:
            high = mid
    return None

unsorted = [5, 1, 6, 2, 10]
sorted = selection_sort(unsorted)
print(binary_search(sorted, 2))