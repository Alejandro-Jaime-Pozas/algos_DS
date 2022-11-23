# better than bogo_sort, selection_sort
import random
# numbers = [5, 3, 7, 2, 3, 8, 9]
numbers = [random.randint(0, 1000) for _ in range(1001)]

def merge_sort(values):
    if len(values) <= 1:
        return values
    midpoint = len(values) // 2
    left_values = merge_sort(values[:midpoint])
    right_values = merge_sort(values[midpoint:])
    sorted_values = []
    left_index = 0
    right_index = 0
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]
    return sorted_values

# print(numbers)
print(merge_sort(numbers))