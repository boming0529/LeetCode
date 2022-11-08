# Definition for a binary tree node.
import math 
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # using BFS (queue)
        n = 1
        queue = deque([(root, n)])
        # pre = (pre_val, pre_level)
        pre = (None, 0)
        while queue:
            (root, n) = queue.popleft()
            #print(root.val , n, pre)
            h = math.log2(n) // 1
            if h > pre[1]:
                pre = (None, pre[1])
            if root:
                if h % 2: # odd level
                    if root.val % 2: # odd number
                        #print('odd level need even number')
                        return False 
                    if pre[0] and pre[0] <= root.val: # increasing functin
                        #print('odd level need decreasing')
                        return False
                else: # even level
                    if not (root.val % 2): # even number
                        #print('even level odd number')
                        return False
                    if pre[0] and pre[0] >= root.val: # decreasing function
                        #print('even level need increasing')
                        return False
                # handle last node for this level
                pre = (root.val, h)
            
                if root.left:
                    #print(f'left here {2*n} ', root.left.val)
                    queue.append((root.left, 2*n))
                if root.right:
                    #print(f'left right {2*n+1} ', root.right.val)
                    queue.append((root.right, 2*n+1))
                    
        return True