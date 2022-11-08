# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : return []
        # using BFS
        h = 1
        res, queue =  [], deque([(root, h)])
        level = []
        while queue:
            root, node_h = queue.popleft()
            if node_h != h:
                h = node_h
                res.append(level)
                level = []
            if root:
                level.append(root.val)
                queue.append((root.left, h+1))
                queue.append((root.right, h+1))
        return res
            