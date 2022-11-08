# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # using inorder Traversal via DFS (Stack) 
        # inorder traversal can sort asc
        stack = [(root, False)]
        smaller, fisrt, pre = 0, True, None
        while stack and (smaller > 1 or fisrt):
            root, traversed = stack.pop()
            if root:
                if traversed:
                    if pre is not None:
                        smaller = (root.val - pre) if (root.val - pre) < smaller or fisrt else smaller
                        fisrt = False
                    pre = root.val
                else:
                    stack.append((root.right, False))
                    stack.append((root, True))
                    stack.append((root.left, False))
        return smaller

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# [90,69,null,49,89,null,52]
# root = TreeNode(90)
# root.left = TreeNode(69)
# root.left.left = TreeNode(49)
# root.left.right = TreeNode(89)
# root.left.left.right = TreeNode(52)

# [0,null,2236,1277,2776,519]
root = TreeNode(0)
root.right = TreeNode(2236)
root.right.left = TreeNode(1277)
root.right.right = TreeNode(2776)
root.right.left.left = TreeNode(519)

ans = Solution().minDiffInBST(root)
print(ans)
assert ans == 1, 'This answer was 1'

