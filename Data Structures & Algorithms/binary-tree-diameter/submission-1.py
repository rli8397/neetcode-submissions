class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return self.res