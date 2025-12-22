from typing import Optional
"""Only pass 22.98%"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(root):
            if root is None:
                # We find the value max value rob with root and withouroot, since the
                # value change so much when we don't append root and when we append root
                # [withRoot, withoutRoot]
                return [0, 0]
        
            leftVal = dfs(root.left) # traverse to find the value in each test case
            # SInce the left and right root is node been affect of the condition of the problem
            rightVal = dfs(root.right)

            withRoot = root.val + leftVal[1] + rightVal[1]
            withoutRoot = max(leftVal) + max(rightVal)

            return [withRoot, withoutRoot]
        
        return max (dfs(root))

        