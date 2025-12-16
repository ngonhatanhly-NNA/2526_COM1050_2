from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        q = deque([(root, root.val)])

        while q:
            node, curr_val = q.popleft()
            
            if curr_val == targetSum and (node.left is None  and node.right is None):
                return True
            if node.left:
                q.append((node.left, curr_val + node.left.val))
            if node.right:
                q.append((node.right, curr_val + node.right.val))
            
        return False