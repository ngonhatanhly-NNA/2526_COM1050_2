from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        q = deque([root])
        
        while q:
            size = len(q)
            path = []
            
            for _ in range (size):
                node = q.popleft()  
                path.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.rigth:
                    q.append(node.right)

            res.append(path)

        return res
            