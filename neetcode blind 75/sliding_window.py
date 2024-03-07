


# def characterReplacement(s, k):
#     # you can change any char you want from s in order to achieve the maximum consecutive letters in a row, only limit is you have to do it in at most k times.
#     # essentially, 
#     if k >= len(s):
#         return k
#     count = {}
#     res = 0

#     l = 0
#     for r in range(len(s)):
#         count[s[r]] = count.get(s[r], 0) + 1 # adding 1 if letter already seen and in count dict

#         while (r - l + 1) - max(count.values()) > k:
#             count[s[l]] -= 1
#             l += 1

#         res = max(res, r - l + 1)
#     return res 


# print(characterReplacement('ABABBCCCCCACCCC', 1))


# def lengthOfLongestSubstring(s):
#     # iterate through string
#     # check if new char already seen
#     # if seen, then add length if it's longest length yet, then move cursor to location of previous repeat char ie "abca" would move cursor to index 1: 'b' but don't iterate again through everything, just continue iterating
#     # how move cursor? need mapping so dict or list or str with indexes. dict would be best i think. key = char, value = index
#     # move cursor to prev repeat char key's index position from dict
#     seen = set()
#     l = 0
#     final = 0
#     for r in range(len(s)):
#         while s[r] in seen:
#             seen.remove(s[l])
#             l += 1
#         seen.add(s[r])
#         final = max(final, r - l + 1)
#     return final

# print(lengthOfLongestSubstring("abac"))

# def maxProfit(prices):
#     # O(n)
#     l,r = 0,1
#     maxP = 0
#     while r < len(prices):
#         if prices[l] < prices[r]:
#             profit = prices[r] - prices[l]
#             maxP = max(profit, maxP)
#         else:
#             l = r  # take l all the way to r's index
#         r += 1

#     return maxP

#     # if no profit can be achieved return 0. 
#     # given a list of prices of one stock, return the max profit achievable, buy price being always before the sell price. 
#     # can do the 2 pointers solution, will always be future - present
#     buy = min(prices)
#     for i,n in enumerate(prices):
#         if n == buy:
#             return max(prices[i:]) - buy
#     # smaller number on the left should go with max on the right

# print(maxProfit([7,2,5,1,3]))