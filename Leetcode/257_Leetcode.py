from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res

        def findPath(node, path):
            
            path += str(node.val)
            
            if node and  node.left is None and node.right is None:
                res.append(path)
                return 
            
            if node.left:
                findPath(node.left, path + '->')
            if node.right:
                findPath(node.right, path + '->')

        findPath(root, "")
        return res
            

