# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or falseotherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def palindrome(string):
    # input: string
    # output: bool
    final = ""
    for c in string.lower():
        if c.isalnum(): #O(1)
            final += c
    return final == final[::-1]

print(palindrome("A man, a plan, a canal: Panama"))
print(palindrome("race a car"))
print(palindrome(" "))