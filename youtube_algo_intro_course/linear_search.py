# BIG O(n)
def linear_search(list: list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None 

def verify(index):
    if index is not None:
        print('target found at index:', index)
    else:
        print('target not in list')

numbers = [num for num in range(1,11)]

print(verify(linear_search(numbers, 11)))