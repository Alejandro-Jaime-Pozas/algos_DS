


# # merge two sorted lists
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         head = ListNode()
#         tail = head

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next 
#             tail = tail.next # this to traverse the new list
#             print('head', head.val)
#             print('tail', tail.val)

#         if l1:
#             tail.next = l1 
#         elif l2:
#             tail.next = l2 
#         print(tail.next.val)

#         return head.next
    

# n1 = ListNode(30)
# n2 = ListNode(20, n1)
# n3 = ListNode(10, n2)
# n4 = ListNode(130)
# n5 = ListNode(120, n4)
# n6 = ListNode(110, n5)
# sol = Solution().mergeTwoLists(n3, n6)
# print()
        


# Reverse linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head):
#         prev, curr = None, head 

#         while curr:
#             curr_next = curr.next 
#             curr.next = prev
#             prev = curr 
#             curr = curr_next
#         return prev 
    

# n1 = ListNode(30)
# n2 = ListNode(20, n1)
# n3 = ListNode(10, n2)
# sol = Solution().reverseList(n3)
# print(sol.val, sol.next.val)