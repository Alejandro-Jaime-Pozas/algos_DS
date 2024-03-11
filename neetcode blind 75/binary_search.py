def search(nums, target):
    # check if target num is in rotated list in O(log n) time
    # could choose a midpoint. based on that midpoint, compare midpoint and l/r
    # if target between l and m, check left side, else check right side
    res = -1
    l, r = 0, len(nums)-1
    while l <= r:
        m = (l + r) // 2
        if target == nums[m]: 
            res = m 
            break
        elif target > nums[m] and (target <= nums[r] or target >= nums[r] <= nums[m]):
            l = m + 1
        else:
            r = m - 1
    return res 

print(search([7,8,4,4,5,6], 6))


# def findMin(nums):
#     # base concept: if you pick middle of the list and that number is > nums[0], then the min has to be either num[0] or a number o the right of middle
#     res = nums[0]
#     l, r = 0, len(nums)-1

#     while l <= r:
#         if nums[l] < nums[r]:
#             res = min(res, nums[l])
#             break
#         m = (l + r) // 2
#         res = min(res, nums[m])
#         if nums[m] >= nums[l]:
#             l = m + 1
#         else:
#             r = m - 1

#     return res

# print(findMin([2,3,4,5,1]))
