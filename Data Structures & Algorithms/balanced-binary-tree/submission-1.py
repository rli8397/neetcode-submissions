# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:Optional[TreeNode]):
            if not node: 
                return (0, True)
            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l[0] - r[0]) > 1:
                return (1 + max(l[0], r[0]), False)
            return (1 + max(l[0], r[0]), (l[1] and r[1]))

        return dfs(root)[1]