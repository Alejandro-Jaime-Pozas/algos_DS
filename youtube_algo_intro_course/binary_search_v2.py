from linear_search_v2 import names, search_names


def binary_search(collection, target):
    first = 0
    last = len(collection) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if collection[midpoint] == target:
            return midpoint
        elif collection[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None 

for n in search_names:
    index = binary_search(names, n)
    print(n, 'at index:', index)
