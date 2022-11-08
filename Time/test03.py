# -*- coding : utf-8 -*-
# from collections import deque # BFS Solution
from typing import Optional

class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def getTreeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        # i using DFS (stack) inorder Traversal to Solution this problem 
        # but i shoud morris algorithm is better then DFS
        max_height = 1
        stack = [(root, False , 1)]
        while stack:
            root, traversed ,h = stack.pop()
            
            if root :
                if traversed:
                    max_height = max_height if max_height > h else h # mean max_height = max(max_height, h)
                    print(root.val , h)
                else:
                    stack.append((root.right, False, h+1))
                    stack.append((root, True, h))
                    stack.append((root.left, False, h+1))

        return max_height

root = TreeNode(60)
root.left = TreeNode(41)
root.left.left = TreeNode(16)
root.left.left.right = TreeNode(25)
root.left.right = TreeNode(53)
root.left.right.left = TreeNode(46)
root.left.right.left.left = TreeNode(42)
root.left.right.right = TreeNode(55)

root.right = TreeNode(74)
root.right.left = TreeNode(65)
root.right.left.left = TreeNode(63)
root.right.left.left.left = TreeNode(62)
root.right.left.left.right = TreeNode(64)
root.right.left.right = TreeNode(70)

assert Solution().getTreeHeight(root) == 5, 'the height should be 5'