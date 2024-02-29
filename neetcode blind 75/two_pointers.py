def threeSum(nums):
    # only distinct triplets should be returned, so if same num even though different index in nums, should not include in final output
    # is there a way this is not n^3?
    # maybe 2 for loops and the nested one already has 2 pairs, just need to check if last pair in list?
    # if -1, need to other nums that sum to 1. if 3 need other 2 nums that sum to -3. but in order to do that, still need to run through n^2
    set_threesum = set(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == i:
                continue
            pair_sum = nums[i] + nums[j]
            # if missing num in nums, then it's a valid pair
            if -pair_sum in set_threesum:

    return 

print(threeSum([-1,0,1,2,-1,-4]))


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