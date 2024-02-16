import random


def selection_sort(values):

    sorted_list = []
    for i in range(0, len(values)):
        # print("%-25s %-25s" % (values, sorted_list))
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i 
    return min_index
    
    # final_list = []
    # while list:
    #     min = list[0] # should also acct for negative numbers in list 
    #     for num in list:
    #         if num < min:
    #             min = num 
    #     min = list.pop(list.index(min))
    #     final_list.append(min)
    # return final_list 


print(selection_sort([8,5,1,4,7,]))
# print(selection_sort([random.randint(1,10000) for _ in range(10000)]))
# print(selection_sort([random.randint(1,10000) for _ in range(1000000)]))