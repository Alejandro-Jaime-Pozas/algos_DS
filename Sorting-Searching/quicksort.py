# better than bogo_sort, selection_sort
numbers = [5, 3, 7, 2, 3, 8, 9]

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print(less_than_pivot, pivot, greater_than_pivot)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
# print(numbers)
print(quicksort(numbers))