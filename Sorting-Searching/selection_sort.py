numbers = [5, 3, 7, 2, 3]

def selection_sort(alist):
    # given a list, sort it by looping and adding to new list
    sorted_list = []
    while len(alist) > 1:
        min_value = alist[0]
        for i in range(len(alist)-1):
            if alist[i+1] <= alist[i]:
                min_value = alist[i+1]
            # print(alist, sorted_list)
        sorted_list.append(alist.pop(alist.index(min_value)))
    sorted_list.append(alist.pop()) if len(alist) == 1 else None
    return sorted_list

print(selection_sort(numbers))