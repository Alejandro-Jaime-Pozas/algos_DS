# 347. Top K Frequent Elements
def topKFrequent(nums, k):
    # so while k > 1 check which numbers are most frequent
    # input -> list of ints, int
    # output -> list of 0 or more ints
    # edge -> what if there is a tie for a number?
    # brute force solution w/o time-complexity
    d = {}
    final = []
    for num in set(nums):
        d[nums.count(num)] = num
    while k > 0:
        # bsically get the max number from d, add to final
        k -= 1
    return

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))


# # 49. Group Anagrams - O(m*n) - m is the len of list, n the len of str
# from collections import defaultdict
# def groupAnagrams(strs):
#     res = defaultdict(list) # mapping charCount to list of Anagrams
#     # defaultdict() takes in a fn like list, int, str, where the default value of the dict would be [], 0, "", accordingly

#     for s in strs:
#         count = [0] * 26 # a ... z
#         for c in s:
#             count[ord(c) - ord("a")] += 1

#         res[tuple(count)].append(s) # tuple bc lists cannot be keys: keys must be immutable objects types
#     return res.values()

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# # Input: strs = ["eat","tea","tan","ate","nat","bat"]
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#     # need to group strings which are anagrams together in lists
#     # input list of strings
#     # output list of lists of strings
#     # create empty list
#     # for loop: for each word in strs, if word...esta dificil..
    # anagrams = []
    # for word in strings:
    #     for group in anagrams:
    #         # if the word is anagram of a group, append to that group
    #         if sorted(word) == sorted(group[0]):
    #             group.append(word)
    #             break
    #     # if word not anagram of an existing group, create new group
    #     else:
    #         anagrams.append([word])

    # return anagrams

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# 1. Two Sum
# class Solution:
# def twoSum(nums, target):

    # # could check for each num..if target - num is in set would still be n^2.
    # # numbers can repeat in array
    # # return list of two index positions of added numbers in any order
    # # if number is > target, disregard
    # # try brute force solution first
    # seen = {}
    # for i, num in enumerate(nums):
    #     # if num is already in dict and target / 2 == num, return indexes
    #     if num in seen and num*2 == target:
    #         return [i, seen[num]]
    #     # if target - num is in dict, return indexes
    #     if target - num in nums and target / 2 != num:
    #         return [i, nums.index(target-num)]
    #     # add the num to dict of seen numbers to check for dupplicates
    #     seen[num] = i
    # return 'no nums add to target'

# Solution 2
#     prevMap = {}
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in prevMap:
#             return [prevMap[diff], i]
#         prevMap[n] = i

# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,1, 9, 9, 10, 6, 7,3], 6))


# 242. Valid Anagram
# def isAnagram(s, t):
#     if len(s) != len(t):
#         return False
#     countS, countT = {}, {}

#     for i in range(len(s)):
#         countS[s[i]] = 1 + countS.get(s[i], 0)
#         countT[t[i]] = 1 + countT.get(t[i], 0)
#     for c in countS:
#         if countS[c] != countT.get(c, 0):
#             return False

#     return True
    
# print(isAnagram('raceacar', 'racaecar'))
# print(isAnagram('raceacar', 'racaecarr'))


# 240. Repeat Values
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
# #         could loop through each elem 
# #         easy solution:
#         for num in nums:
#             if nums.count(num) > 1:
#                 return True
#         return False