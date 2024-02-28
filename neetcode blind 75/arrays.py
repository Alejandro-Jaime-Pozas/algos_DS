def topKFrequent(nums, k):
    # Big O n log n
    # need to compare items in array with one another
    # could create dict/hash where item is key, value counts number of that key
    # in the end, have dict with different values, would need to sort or somehow get the key of the highest k values...
    # sorting should work, will be process independent of getting the counts of each list item, good for time complexity
    if not nums: return [0]

    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    counts = [item for item in counts.items()]
    counts.sort(key=lambda tup: tup[1], reverse=True)

    # return type(counts)
    return [tup[0] for tup in counts][:k]
    

print(topKFrequent([1,1,1,1,2,3,2,2,3,3,3,4], 2))


# from collections import defaultdict

# def groupAnagrams(strs):
#     res = defaultdict(list) # mapping charCount to list of Anagrams
#     # defaultdict() takes in a fn like list, int, str, where the default value of the dict would be [], 0, "", accordingly

#     for s in strs:
#         count = [0] * 26 # a ... z
#         for c in s:
#             count[ord(c) - ord("a")] += 1

#         res[tuple(count)].append(s) # tuple bc lists cannot be keys: keys must be immutable objects types
#     print(res)
#     return res.values()

# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# # 128. Longest Consecutive Sequence - O(n)
# def longestConsecutive(nums):
#     # neetcode
#     num_set = set(nums)
#     longest = 0

#     for n in nums:
#         # check if n is the start of a sequence
#         if (n - 1) not in num_set:
#             length = 0
#             while (n + length) in num_set:
#                 length += 1
#             longest = max(length, longest)
#     return longest

#     # need to sort? can keep track of numbers..maybe wo sorting
#     # looking for consecutive numbers. could mean either n+1 or n-1..
#     # can store each num in hash, check if n-1 or n+1 in hash, create another hash to store counting lengths..final for loop to check hash items of counting lengths, return highests num (max)
#     # cannot only look for n-1 or n+1, need to look at all prev values
#     if not nums:
#         return 0
#     # nums.sort() # you cant sort
#     values = {}
#     count = 1
#     for i in range(len(nums)-1):
#         if nums[i+1] == nums[i] + 1:
#             count += 1
#         elif nums[i+1] == nums[i]:
#             continue
#         else:
#             values[nums[i]] = count
#             count = 1
#     else:
#         values['only_one'] = count
#         count = 1
#     maxn = 0
#     for length in values.values():
#         if length > maxn:
#             maxn = length
#     print(values)
#     return maxn

# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1,10]))

# # encode and decode strings (premium) - O(n)
# class Solution:
#     """
#     @param: strs: a list of strings
#     @return: encodes a list of strings to a single string.
#     """

#     def encode(self, strs):
#         res = ""
#         for s in strs:
#             res += str(len(s)) + "#" + s
#         return res

#     """
#     @param: s: A string
#     @return: decodes a single string to a list of strings
#     """

#     def decode(self, s):
#         res, i = [], 0

#         while i < len(s):
#             j = i
#             while s[j] != "#":
#                 j += 1
#                 print(s[j])
#             length = int(s[i:j])
#             # print(length)
#             res.append(s[j + 1 : j + 1 + length])
#             i = j + 1 + length
#         return res

# s = Solution()
# encoded = s.encode(['i', 'am', 'the', 'wal#rus'])
# print(encoded)
# decoded = s.decode(encoded)
# print(decoded)


# # 238. product of array except self - O(n)
# def productExceptSelf(nums):
#     # one way would be for loop for every num..inefficient
#     # another way is to store values, then multiply all of them except for num in the for loop...
#     # cannot divide by 0

#     # ===============
#     res = [0] * len(nums)
#     prefix = 1
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix *= nums[i]
#     postfix = 1
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] *= postfix
#         postfix *= nums[i]
#     return res 

    # # ==============
    # # another is you can muliply everything (except 0s) then divide by current num in for loop ()
    # # get the max product of all nums multiplied except for 0s
    # product = 1
    # zeros = 0
    # for num in nums:
    #     if num != 0:
    #         product *= num
    #     else:
    #         zeros += 1
    # # for num in nums, if 2 or more zeros, append 0, if 1 zero and num == 0, append product else 0, if no zeros divide product by num
    # final = []
    # for num in nums:
    #     if zeros > 1:
    #         final.append(0)
    #     elif zeros == 1:
    #         if num == 0:
    #             final.append(product)
    #         else:
    #             final.append(0)
    #     else:
    #         final.append(product // num)
    # return final

    # ===============
    # # let's try the inefficient way
    # final = []
    # for i, num in enumerate(nums):
    #     product = 1
    #     for j, multiply_by in enumerate(nums):
    #         if i != j:
    #             product *= multiply_by
    #     final.append(product)
    # return final

# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))
# print(productExceptSelf([-1,1,0,-3,3,0]))
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# # 347. Top K Frequent Elements - O(n) bucket sort
# def topKFrequent(nums, k):
#     # instead of doing nums.count...for loop through all array, add value to count of d
#     # 
#     count = {}
#     freq = [[] for i in range(len(nums)+1)]
#     for n in nums: 
#         count[n] = count.get(n, 0) + 1
#     for n, c in count.items():
#         freq[c].append(n)
    
#     res = []
#     for i in range(len(freq)-1, 0, -1): # taking the reverse freq list start at end and end at start
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k:
#                 return res

# print(topKFrequent(nums = [1,1,1,2,2,3,2,2,2,2,3], k = 2))
# print(topKFrequent(nums = [1], k = 1))
# print(topKFrequent(nums = [], k = 1))

    # # so while k > 1 check which numbers are most frequent
    # # input -> list of ints, int
    # # output -> list of 0 or more ints
    # # edge -> what if there is a tie for a number?
    # # brute force solution w/o time-complexity
    # d = {}
    # final = []
    # for num in set(nums):
    #     d[nums.count(num)] = num
    # # print(d.keys())
    # while k > 0 and nums:
    #     # bsically get the max number from d, add to final
    #     # final.append(d[max(d.keys())])
    #     # d.pop(max(d.keys()))
    #     sorted_keys = sorted(d.keys(), reverse=True)
    #     max_num = sorted_keys[0]
    #     final.append(d[max_num])
    #     d.pop(max_num)
    #     k -= 1
    # return final



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