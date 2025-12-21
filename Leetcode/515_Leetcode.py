from typing import Optional, List

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            size = len(q)
            curr_max = float('-inf')

            for _ in range (size):
                node = q.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(curr_max)

        return res