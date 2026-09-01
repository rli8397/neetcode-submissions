# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. if the current node val is in between p and q, then it is the LCA
# 2. if the current node val is = to p or q, then it is the LCA
# 3. if the current node val is greater or less than both p or q, the traverse to that side of the tree
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        def lcaRecurse(node: TreeNode) -> TreeNode:
            if not node: return None
            if p.val <= node.val <= q.val: return node
            if node.val > q.val: return lcaRecurse(node.left)
            return lcaRecurse(node.right)

        return lcaRecurse(root)