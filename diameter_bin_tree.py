class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def dfs(root):
            if root is None:
                return 0
            L = dfs(root.left)
            R = dfs(root.right)
            self.maxi = max(self.maxi, L+R+1)
            return max(L,R)+1
        
        dfs(root)
        return self.maxi -1
