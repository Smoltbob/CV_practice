      def dfs(root, upper,lower):
            if not root:
                return True
                     
            if root.val <= lower or root.val >= upper:
                    return False
                
            res = dfs(root.left, upper=root.val,lower=lower) and                                                             dfs(root.right,upper=upper,lower=root.val)
             
            return res
        
        return dfs(root, upper=float('inf'), lower=float('-inf'))
                
