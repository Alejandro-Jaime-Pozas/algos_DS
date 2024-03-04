def maxProfit(prices):
    # O(n)
    l,r = 0,1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(profit, maxP)
        else:
            l = r 
        r += 1

    return maxP 

    # if no profit can be achieved return 0. 
    # given a list of prices of one stock, return the max profit achievable, buy price being always before the sell price. 
    # can do the 2 pointers solution, will always be future - present
    buy = min(prices)
    for i,n in enumerate(prices):
        if n == buy:
            return max(prices[i:]) - buy
    # smaller number on the left should go with max on the right

print(maxProfit([7,2,5,1,3]))

# # CONTAINER WITH MOST WATER
# def maxArea(height):
#     # PROPER SOLUTION O(n)
#     final = 0
#     l, r = 0, len(height)-1
#     while l < r:
#         water = (r-l) * min(height[l], height[r])
#         final = max(final, water)
#         if height[l] < height[r]:
#             l += 1
#         else:
#             r -= 1
#     return final 

#     # BRUTE FORCE MY SOLUTION
#     # think i could loop through list, take that number and get very possible outcome, and just have a variable max set, and update if there is a greater value, then do the same for next iterations...
#     # this would be n^2, is there way to do n log n? or more efficient version like k * n
#     final = 0
#     for i,n in enumerate(height):
#         for j in range(i+1, len(height)):
#             # check n vs n2, final should update if the product of (j-i) * min(n, n2) is > final...
#             water = (j-i) * min(n, height[j])
#             print(i, ',', j, '=', water)
#             if water > final:
#                 final = water
#             # could be way to check the distance and nums when final updates, so as to stop the code if max limit has been achieved
#     return final 

# # print(maxArea([1,1]))
# print(maxArea([1,8,7,1,1,1,1,6]))

# def threeSum(nums):
#     res = []
#     nums.sort()

#     for i, a in enumerate(nums):
#         if i > 0 and a == nums[i-1]:
#             continue 

#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             threeSum = a + nums[l] + nums[r]
#             if threeSum > 0:
#                 r -= 1
#             elif threeSum < 0:
#                 l += 1
#             else:
#                 res.append([a, nums[l], nums[r]])
#                 l += 1
#                 while nums[l] == nums[l - 1] and l < r:
#                     l += 1
#     return res

# print(threeSum([2,7,11,15, -2, 0, 1, -1]))


# MY SOLUTION
# def threeSum(nums):
#     # only distinct triplets should be returned, so if same num even though different index in nums, should not include in final output
#     # is there a way this is not n^3?
#     # maybe 2 for loops and the nested one already has 2 pairs, just need to check if last pair in list?
#     # if -1, need to other nums that sum to 1. if 3 need other 2 nums that sum to -3. but in order to do that, still need to run through n^2
#     counts = {}
#     final = []
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             # if same index, ignore
#             if i == j:
#                 continue
#             pair_sum = nums[i] + nums[j]
#             # if missing num in nums, then it's a valid threesum
#             # check if third num needed exists and that it's not repeat of i or j
#             third = counts.get(-pair_sum) or 0
#             # if third num exists in counts
#             if third > 0:
#                 # if third num equals num at i or j, then check there's more than 2 same nums, else store triplet and check in end if same triplets and eliminate them
#                 if nums[i] == -pair_sum:
#                     if third <= 1:
#                         break
#                 elif nums[j] == -pair_sum:
#                     if third <= 1:
#                         break 
#                 # check if triplet already in final, append if not
#                 else:
#                     triplet = [nums[i], nums[j], -pair_sum]
#                     final.append(triplet) if triplet not in final else None 

#     true_final = []
#     for t in final:
#         for num in t:
#             pass

# print(threeSum([-1,0,1]))


# def isPalindrome(s):
#     is_palindrome = [c for c in s.lower() if c.isalnum()]
#     # return is_palindrome == is_palindrome[::-1]
#     left, right = 0, len(is_palindrome)-1
#     while left < right:
#         if is_palindrome[left] != is_palindrome[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# print(isPalindrome("race car"))