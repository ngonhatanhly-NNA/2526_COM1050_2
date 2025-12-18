from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def findPath(root, current_path, current_sum):
            if not root:
                return
            current_sum += root.val
            current_path.append(root.val)

            if not root.left and not root.right:
                if current_sum == targetSum:
                    res.append(list(current_path))

            leftCheck = findPath(root.left, current_path, current_sum)
            rightCheck = findPath(root.right, current_path, current_sum)

            current_path.pop()

        findPath(root, [], 0)
        return res


        