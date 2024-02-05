
def binary_search(list, target):
    first = 0
    last = len(list)-1
    iterations = 0

    while first <= last:
        midpoint = (first + last) // 2
        # iterations += 1
        if list[midpoint] == target:
            return midpoint 
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None 

numbers = [x for x in range(10)]

print(binary_search(numbers, 1))