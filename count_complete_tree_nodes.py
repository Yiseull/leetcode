from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        return self.countNodes(node.left) + self.countNodes(node.right) + 1