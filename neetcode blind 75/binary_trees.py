# Subtree of another tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subroot) -> bool:
        # same as same tree, but in this case check starts when subroot initial val is found in root
        # will need to traverse w/recursion or BFS
        # for every value in root that equals top subroot value, will need to check
        # will need a general iteration through entire root (until match found), then inner for loop iteration when the top value in subroot matches current root iteration

        # GLOBAL ROOT SCOPE

        # Base case
        if (not root and subroot) or (root and not subroot):
            # at tree leaf, return root. doesn't matter what you return, just to end execution
            return False
        elif not root and not subroot:
            return True
        # if root = subroot then traverse both and return true if true
        elif root.val == subroot.val:
            left = self.isSubtree(root.left, subroot.left)
            right = self.isSubtree(root.right, subroot.right)
        # if subroot value is not = root value, then keep traversing root until end
        while root.val != subroot.val:


        # traverse the curr root's left and right nodes. input subroot to check if equal in each






# # Same tree
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p, q) -> bool:
#         # p and q are the roots of 2 different binary trees.
#         # check if all p values = q values and structure is the same, if not return false
#         # will need to traverse both trees, same time and compare if node/null an if values are equal
#         if not p:
#             if q:
#                 # means not same, return False
#                 return False
#             # else means p and q both None nodes with no value, this is last tree leaf so return True
#             return True
#         if p:
#             if not q or p.val != q.val:  # means not same, return False
#                 return False
#         # missing if p and q are equal, what to do?
#         left = self.isSameTree(p.left, q.left)  # returns True/False
#         right = self.isSameTree(p.right, q.right)  # returns True/False
#         return left == right == True  # which returns True/False


# n3 = TreeNode(20)
# n2 = TreeNode(9)
# n1 = TreeNode(3, n2, n3)
# n30 = TreeNode(20)
# n20 = TreeNode(9)
# n10 = TreeNode(3, n20, n30)
# # Solution().isSameTree(n1, n10)
# print(Solution().isSameTree(n1, n10))



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

