# Reorder list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle node by traversing list twice,
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


n1 = ListNode(6)
n2 = ListNode(5, n1)
n3 = ListNode(4, n2)
n4 = ListNode(3, n3)
n5 = ListNode(2, n4)
n6 = ListNode(1, n5)
sol = Solution().reorderList(n6)



# # merge two sorted lists
#     # each list starts with its head node
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         head = ListNode()
#         tail = head  # can be confusing, see below

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             print('head', head.val)
#             print('tail', tail.val)
#             tail = tail.next # this to traverse the new list; this reassigns tail to its next value, leaving head unchanged

#         if l1:
#             tail.next = l1
#         elif l2:
#             tail.next = l2
#         # print(tail.next.val)

#         return head.next  # this works bc initially, tail = head creates a copy of head


# n1 = ListNode(30)
# n2 = ListNode(20, n1)
# n3 = ListNode(10, n2)
# n4 = ListNode(130)
# n5 = ListNode(120, n4)
# n6 = ListNode(110, n5)
# sol = Solution().mergeTwoLists(n3, n6)



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