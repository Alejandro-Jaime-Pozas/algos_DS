# this seems to first go into the first quicksort(less_than_pivot) recursively until reaching base case, then to the other quicksort recursive once base case for first is returned
def quicksort(values):
    '''
    O(n^2) worst case if you always choose the first value as pivot and list is reverse sorted
    on average, O(n log n) if the pivot is chosen at random (or maybe in the middle of list)
    '''
    if len(values) <= 1:
        # print('base case reached for values: ', values )
        return values 
    less_than_pivot = []
    more_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            more_than_pivot.append(value)
    # print("%15s %1s %15s" % (less_than_pivot, [pivot], more_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(more_than_pivot)

if __name__=="__main__":
    print(quicksort([8,5,1,4,7,100,200,300,3]))
    # print(quicksort([random.randint(1,10000) for _ in range(10000)]))
    # print(quicksort([random.randint(1,10000) for _ in range(1000000)]))