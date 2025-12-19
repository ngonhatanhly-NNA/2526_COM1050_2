from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class MySolution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        left_to_right = True
        
        while q:
            size = len(q)
            current_level = deque()
            for _ in range (size):
                node = q.popleft()
                
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(list(current_level))
            left_to_right = not left_to_right
        
        return res

