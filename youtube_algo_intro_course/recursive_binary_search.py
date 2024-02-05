def recursive_binary_search(list, target):
    if len(list) == 0:
        return False 
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True 
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

print(recursive_binary_search([1,2,3,4,5,6,7,8], 12))
print(recursive_binary_search([1,2,3,4,5,6,7,8], 6))

print(10//2)