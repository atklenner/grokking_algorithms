def quicksort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        pivot = unsorted_list[0]
        lower = [item for item in unsorted_list if item < pivot]
        greater = [item for item in unsorted_list if item > pivot]
        return quicksort(lower) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))