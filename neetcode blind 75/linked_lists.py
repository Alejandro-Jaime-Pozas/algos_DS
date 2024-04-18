# Same tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        # p and q are the roots of 2 different binary trees.
        # check if all p values = q values and structure is the same, if not return false
        # will need to traverse both trees, same time and compare if node/null an if values are equal
        if not p:
            if q:
                # means not same, return False
                return False
            # else means p and q both None nodes with no value, this is last tree leaf so return True
            return True
        if p:
            if not q or p.val != q.val:  # means not same, return False
                return False
        # missing if p and q are equal, what to do?
        left = self.isSameTree(p.left, q.left)  # returns True/False
        right = self.isSameTree(p.right, q.right)  # returns True/False
        return left == right == True  # which returns True/False


n3 = TreeNode(20)
n2 = TreeNode(9)
n1 = TreeNode(3, n2, n3)
n30 = TreeNode(20)
n20 = TreeNode(9)
n10 = TreeNode(3, n20, n30)
# Solution().isSameTree(n1, n10)
print(Solution().isSameTree(n1, n10))



# # Maximum depth of binary tree
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root) -> int:
#         # Recursive solution
#         if not root:
#             return 0
#         # traverse root's left and right nodes but add + 1 to a variable and in end return it
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#         # # Breadth first solution
#         # from collections import deque
#         # if not root:
#         #     return 0
#         # level = 0
#         # q = deque([root])
#         # while q:
#         #     for i in range(len(q)):
#         #         node = q.popleft()
#         #         if node.left:
#         #             q.append(node.left)
#         #         if node.right:
#         #             q.append(node.right)
#         #     level += 1
#         # return level

# n5 = TreeNode(15)
# n4 = TreeNode(7)
# n3 = TreeNode(20, n5, n4)
# n2 = TreeNode(9)
# n1 = TreeNode(3, n2, n3)
# Solution().maxDepth(n1)


# # Invert binary tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root):
#         # need to somehow switch all nodes with a parent from parent's left to right and vice versa
#         # while there is a node at parent's left or right
#         # this is a recursive fn.
#         # if there is no root node in this iteration, return None
#         if not root:
#             return None

#         # if root, switch its left and right children
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp

#         self.invertTree(root.left)  # this is the new root in next iter
#         self.invertTree(root.right)  # this is the new root in next iter
#         return root

#     # in the base case you want to return None, since what you're doing is just switching values for left and right of node
# n4 = TreeNode(4)
# n2 = TreeNode(2)
# n7 = TreeNode(7)
# n1 = TreeNode(1)
# n3 = TreeNode(3)
# n6 = TreeNode(6)
# n9 = TreeNode(9)

# n4.left, n4.right = n2, n7
# n2.left, n2.right = n1, n3
# n7.left, n7.right = n6, n9

# print(Solution().invertTree(n4).val)


# # merge k sorted lists
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists):
#         # lists are already sorted in asc order
#         # each item in lists is a ListNode obj startin with the head
#         if not lists or len(lists) == 0:
#             return None

#         while len(lists) > 1:  # keep reducing while there's more than 1 list
#             merged_lists = []

#             for i in range(0, len(lists), 2):  # increments of 2 to grab 2 lists each round so i and i+1
#                 l1 = lists[i]
#                 l2 = lists[i+1] if i + 1 < len(lists) else None
#                 merged_lists.append(self.mergeList(l1, l2))
#             lists = merged_lists
#         return lists[0]


#     def mergeList(self, l1, l2):
#         dummy = ListNode()
#         tail = dummy

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
#         if l1:
#             tail.next = l1
#         if l2:
#             tail.next = l2
#         return dummy.next


# print(Solution.mergeKLists('sme', ['123', '345', None, None]))


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