# Subtree of another tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subroot) -> bool:
        # if there is a root but no subroot, then any children in root have null value equal to subroot, return True
        if not subroot:
            return True
        # if there is no root but is a subroot, that's false since subroot should be in root
        elif not root:
            return False
        # other two cases are covered in sameTree, so run through fn
        elif self.sameTree(root, subroot):
            return True
        else:
            # keep iterating through left and right of root
            left = self.isSubtree(root.left, subroot)
            right = self.isSubtree(root.right, subroot)
            # what if same tree is false for all subtrees? return False
            return left == True or right == True

    def sameTree(self, root, subroot):
        """Check root and subroot's values and all their children's values. If same, return True else False."""
        # if both are None then return True bc they're the same (top-most base case)
        if not root and not subroot:
            return True
        # else if root and subroot exist and have same value
        elif root and subroot and root.val == subroot.val:
            left = self.sameTree(root.left, subroot.left)
            right = self.sameTree(root.right, subroot.right)
            return left == right == True
        # missing if root and not subroot, if not subroot and root; means they're not equal at comparison level, since we're checking for identical trees here in sameTree fn unlike isSubtree fn (where you can have root and no subroot)
        return False

n3 = TreeNode(2)
n2 = TreeNode(1)
n1 = TreeNode(4, n2, n3)
n30 = TreeNode(5)
n20 = TreeNode(4)
n10 = TreeNode(3, n20, n30)
n20.left, n20.right = TreeNode(1), TreeNode(2)
Solution().isSubtree(n1, n10)
# print(Solution().isSubtree(n10, n1))


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

