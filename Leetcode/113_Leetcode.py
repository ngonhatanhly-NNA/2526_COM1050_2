from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum = int) -> List[List[int]]:
        pass

root =  [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
targetSum = 22