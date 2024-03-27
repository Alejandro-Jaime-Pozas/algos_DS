# merge k sorted lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        # lists are already sorted in asc order
        # each item in lists is a ListNode obj startin with the head
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:  # keep reducing while there's more than 1 list
            merged_lists = []

            for i in range(0, len(lists), 2):  # increments of 2 to grab 2 lists each round so i and i+1
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeList(l1, l2))
            lists = merged_lists
        return lists[0]


    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


print(Solution.mergeKLists('sme', ['123', '345', None, None]))


# # Linked list cycle
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head) -> bool:
#         # have a hidden variable in test called pos
#         # pos is the index of the node
#         # so, if a node's next node (tail) is less than original node's index, return True, else False
#         # thinking maybe shortcut knowing the pos..but still need to traverse list anyway
#         # seen = set()
#         # curr = head
#         # while curr:
#         #     if curr in seen:
#         #         return True
#         #     else:
#         #         seen.add(curr)
#         #         curr = curr.next
#         # return False
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         False


# # Remove the nth node from end of list
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head, n: int):
#         # so i think need to traverse the list obviously to get to desired node
#         # nth from end is same as length of list...
#         # options: reverse the list first, then remove link for nth node (but would then need to reset list to original)
#             # traverse list once and get the nth node, then cut link for that node, but since singly linked list, would need to traverse second time knowing that len(list) - nth node + 1 is the node to remove
#         length = 0
#         traverse = head
#         while traverse:
#             length += 1
#             traverse = traverse.next

#         node_to_remove_prev = length - n
#         trav_remove = ListNode()
#         trav_remove.next = head
#         position = 0
#         while trav_remove:
#             # check if ntrp == this iter, means this node.next needs to be removed
#             if node_to_remove_prev == position:
#                 if trav_remove.next.next:
#                     if trav_remove.next == head:
#                         head = trav_remove.next.next
#                     trav_remove.next = trav_remove.next.next
#                 else:
#                     if trav_remove.next == head:
#                         head = None
#                     else:
#                         trav_remove.next = None
#             trav_remove = trav_remove.next
#             position += 1
#         return head
#         # final = []
#         # trav = head
#         # while trav:
#         #     final.append(trav.val)
#             # trav = trav.next


# # n6 = ListNode(6)
# # n5 = ListNode(5, n6)
# # n4 = ListNode(4, n5)
# # n3 = ListNode(3, n4)
# # n2 = ListNode(2, n3)
# # n1 = ListNode(1, n2)
# n1 = ListNode(1)
# sol = Solution().removeNthFromEnd(n1, 1)
# print(sol)

# # Reorder list
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reorderList(self, head):
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         # find middle node by traversing list with 2 pointers
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         # reverse second half
#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         # merge two halfs
#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2


# n1 = ListNode(6)
# n2 = ListNode(5, n1)
# n3 = ListNode(4, n2)
# n4 = ListNode(3, n3)
# n5 = ListNode(2, n4)
# n6 = ListNode(1, n5)
# sol = Solution().reorderList(n6)



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