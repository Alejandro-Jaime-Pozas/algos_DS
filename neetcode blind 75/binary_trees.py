my_dict = {i: value for i, value in enumerate([5,4,3,2])}
print(my_dict)


# # Construct binary tree from preourder and inorder traversal
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder, inorder):
#         # preorder: top down, then left right
#         # inorder: left to right
#         # for some reason need both to construct a binary tree...
#         # all values from each list are included in the other, so same length as well
#         # what's the pattern/algo?
#         # first in preorder is always the root. second could be left/right child of root
#         # as for inorder, everything left of root is to the left, right to the right
#         if not preorder or not inorder:
#             return None
#         root = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
#         return root


# Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])


# # # Kth smallest element in a BST
# # # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root, k) -> int:
#         # bst is an index ordered BST so values are in order smallest to largest left to right
#         # still need to traverse entire tree to find the amount of nodes to return k.
#         # root.left < root < root.right always
#         n = 0
#         stack = []
#         cur = root

#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left

#             cur = stack.pop()
#             n += 1
#             if n == k:
#                 return cur.val
#             cur = cur.right

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# Solution().kthSmallest(root, 3)
# # print(Solution().kthSmallest(root, 3))


# # Validate binary search tree
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isValidBST(self, root) -> bool:

#         def valid(node, left, right):
#             if not node:
#                 return True
#             if not (node.val < right and node.val > left):
#                 return False

#             return valid(node.left, left, node.val) and valid(node.right, node.val, right)
#         return valid(root, float('-inf'), float('inf'))


# r = TreeNode(10)
# r.left = TreeNode(5)
# r.left.left = TreeNode(4)
# r.left.right = TreeNode(6)
# r.right = TreeNode(15)
# r.right.left = TreeNode(9)
# r.right.right = TreeNode(20)
# # Solution().isValidBST(r)
# print(Solution().isValidBST(r))



# # # Binary tree level order traversal
# # # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root):
#         # need to use a deque or queue to pop items from start
#         # while root, add root to level_order_list
#         # then get root.left and root.right and if not None add them
#         # i could initialize the list with first root. or could have 2 lists. one with all same level nodes, other to add those same level nodes' children to the next level
#         from collections import deque
#         level_order_list = []
#         current_nodes = deque([root])
#         while current_nodes:
#             curr_level = []
#             level_size = len(current_nodes)
#             for _ in range(level_size):  # this does not update its range; if added values to current_nodes within loop, doesn't acct for them
#                 node = current_nodes.popleft()
#                 curr_level.append(node.val)
#                 # now go on to next nodes
#                 if node.left:
#                     current_nodes.append(node.left)
#                 if node.right:
#                     current_nodes.append(node.right)
#             level_order_list.append(curr_level) if curr_level else None
#         return level_order_list



# # Example usage:
# # Create a tree
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.left.left = TreeNode(16)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# # Use Solution class to get level order traversal
# sol = Solution()
# print(sol.levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]



# # Lowest common ancestor
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         # need to find the lowest ancestor of both p and q. could be a different node, or p could be ancestor of q or vice versa. there will always be a common ancestor.
#         # essentially need to traverse the tree, check for p and q. as soon as reaching p and q, go back up the tree to search for the common ancestor...
#         # could maybe store the values of nodes already seen but how to recursively include those values?
#         curr = root
#         while curr:
#             if p.val > curr.val and q.val > curr.val:
#                 curr = curr.right
#             elif p.val < curr.val and q.val < curr.val:
#                 curr = curr.left
#             else:
#                 return curr


# n3 = TreeNode(9)
# n2 = TreeNode(3)
# n1 = TreeNode(4)
# n1.left, n1.right = n2, n3
# # n30 = TreeNode(5)
# # n20 = TreeNode(4)
# # n10 = TreeNode(3, n20, n30)
# # n20.left, n20.right = TreeNode(1), TreeNode(2)
# # Solution().lowestCommonAncestor(n1, n2, n3)  # 4
# print(Solution().lowestCommonAncestor(n1, n2, n3).val)


# # Subtree of another tree
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSubtree(self, root, subroot) -> bool:
#         # if there is a root but no subroot, then any children in root have null value equal to subroot, return True
#         if not subroot:
#             return True
#         # if there is no root but is a subroot, that's false since subroot should be in root
#         elif not root:
#             return False
#         # other two cases are covered in sameTree, so run through fn
#         elif self.sameTree(root, subroot):
#             return True
#         else:
#             # keep iterating through left and right of root
#             left = self.isSubtree(root.left, subroot)
#             right = self.isSubtree(root.right, subroot)
#             # what if same tree is false for all subtrees? return False
#             return left == True or right == True

#     def sameTree(self, root, subroot):
#         """Check root and subroot's values and all their children's values. If same, return True else False."""
#         # if both are None then return True bc they're the same (top-most base case)
#         if not root and not subroot:
#             return True
#         # else if root and subroot exist and have same value
#         elif root and subroot and root.val == subroot.val:
#             left = self.sameTree(root.left, subroot.left)
#             right = self.sameTree(root.right, subroot.right)
#             return left == right == True
#         # missing if root and not subroot, if not subroot and root; means they're not equal at comparison level, since we're checking for identical trees here in sameTree fn unlike isSubtree fn (where you can have root and no subroot)
#         return False

# n3 = TreeNode(2)
# n2 = TreeNode(1)
# n1 = TreeNode(4, n2, n3)
# n30 = TreeNode(5)
# n20 = TreeNode(4)
# n10 = TreeNode(3, n20, n30)
# n20.left, n20.right = TreeNode(1), TreeNode(2)
# Solution().isSubtree(n1, n10)
# # print(Solution().isSubtree(n10, n1))


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

