# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Approach 1 : Recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both are none
        if not p and not q:
            return True
        # another is none
        if not (p and q):
            return False
        # val not same
        if p.val != q.val:
            return False
        if not (p or q):
            return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# Approach 2 : Iteration
# https://leetcode.com/problems/same-tree/solution/297064
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS (Stack)
        stack = [(p,q)]
        while stack:
            (p , q) = stack.pop()
            # p, q is exists and val are same
            if p and q  and p.val == q.val:
                # add stack
                stack.extend([
                    (p.right, q.right),
                    (p.left, q.left)
                ])
            elif p or q:
                return False
        return True

    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS (Queue)
        queue = deque([(p,q)])
        while queue:
            (p , q) = queue.popleft()
            # p, q is exists and val are same
            if p and q  and p.val == q.val:
                # add qeueu
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            elif p or q:
                return False
        return True


left_2 = TreeNode(2)
left_3 = TreeNode(3)      
p = TreeNode(1, left_2, left_3)

right_2 = TreeNode(2)
right_3 = TreeNode(3)      
q = TreeNode(1, right_2, right_3)




stack = [(p, q)]
while stack:
    (p,q) =  stack.pop()
    if p and q and p.val == q.val:
        stack.extend([
            (p.left, q.left),
            (p.right, q.right)
        ])

        print('i')
    elif p or q:
        print(False)

print(p)


