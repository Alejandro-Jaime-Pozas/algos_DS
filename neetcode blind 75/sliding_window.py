


# def minWindow(s, t):
#     if t == '': return ''

#     countT, window = {}, {}

#     for c in t:
#         countT[c] = 1 + countT.get(c, 0)

#     have, need = 0, len(countT)
#     res, res_len = [-1, -1], float("infinity")
#     l = 0
#     for r in range(len(s)):
#         c = s[r]
#         window[c] = 1 + window.get(c, 0)

#         if c in countT and window[c] == countT[c]:
#             have += 1

#         while have == need:
#             # update our result in final string
#             if (r - l + 1) < res_len:
#                 res = [l, r]
#                 res_len = (r - l + 1)
#             # pop from the left of window
#             window[s[l]] -= 1
#             if s[l] in countT and window[s[l]] < countT[s[l]]:
#                 have -= 1
#             l += 1

#     l, r = res
#     return s[l:r+1] if res_len != float("infinity") else ""

# print(minWindow("abacab", "bac"))


# def minWindow(s, t):
#     # am missing a way to update t_values correctly...
#     t_values = {}
#     for c in t:
#         t_values[c] = t_values.get(c, 0) + 1

#     min_string = ""
#     t_index_in_s = []
#     counter = 0
#     l = 0
#     # for every letter in 's'
#     for r in range(len(s)):
#         # if letter in 's' matches a letter in 't'
#         if s[r] in t:
#             # add letter to t index in s list to track relevant index positions to move left index to later
#             t_index_in_s.append(r)
#             # then add letter to some dict to keep track of which 't' letters have been found IF THE LETTER IS NOT ALREADY IN SEEN AND MAX OF THAT LETTER HAS BEEN REACHED
#             # if t_values[s[r]] > 0:
#             t_values[s[r]] = t_values.get(s[r],0) - 1
#         # else dont do anything
#         # if all letters from 't' have been found in 's'
#         if max(t_values.values()) <= 0:
#             # if all letters have been found
#                 # if there's extra letters such that value of letter in t_values < 0
#                     # then while s[l] < 0, add t_values[s[l]] + 1
#             # then add that substring to min_string if substring is none OR if length of this substring is <= previous
#             if not min_string or (r - l + 1) <= len(min_string):
#                 min_string = s[l:r+1] # r inclusive
#             # add 1 to the letter in t_values at s[l]
#             t_values[s[r]] = t_values.get(s[r],0) + 1
#             counter += 1
#             # now adjust the left index to position of next letter in 's' that is also part of 't'
#             if len(t_index_in_s) > counter:
#                 l = t_index_in_s[counter] # WHAT IF COUNTER EXCEEDS THE LENGTH OF LIST?
#             # else dont move left index
#         # if no letters from 't' have been found yet, move left to right
#         if sum(t_values.values()) == len(t):
#             l += 1
            
#     return min_string

# print(minWindow("acbbaca", "aba"))


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