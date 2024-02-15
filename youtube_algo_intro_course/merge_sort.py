# CHECK THIS IN PYTHON TUTOR SITE HOW IT WORKS
def merge_sort(list):
    '''
    O(kn log n)

    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: recursively sort the sublists created in prev step
    Combine: merge the sorted sublists created in prev step
    '''

    if len(list) <= 1:
        return list 
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
    

def split(list):
    '''
    O(k log n)
    Divides the unsorted list at mipoint into sublists
    Returns 2 sublists
    '''
    midpoint = len(list) // 2
    return list[:midpoint], list[midpoint:] # index slicing in py takes 'k' time

def merge(left, right):
    '''
    O(n log n)
    Merges 2 lists sorting them in the process
    Returns a new merged list
    '''

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1

    return l 
    
    # # this should be sorting, not sure if 2 values or 2 lists...lists
    # merged = []
    # for i,n in enumerate(left):
    #     if left[i] > right[i]:
    #         merged += [right[i], left[i]]
    #     else:
    #         merged += [left[i], right[i]]
    # return merged


# print([8,7,6,5,4,3,2,1,12,13,14,15][:-5:-1])
# print(merge_sort([8,5]))
print(merge_sort([8,5,7,2,6,4,3,1]))