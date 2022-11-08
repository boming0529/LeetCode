# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Level-Order Traversal via BFS (Queue)
        # Timespace : O(n)
        if root is None:
            return 0
        Queue = [(root, 0)]
        ans = 0
        while Queue:
            node, bitset = Queue.pop(0)
            if node:
                bitset = bitset << 1 | node.val
                if node.left is None and node.right is None: # leaf
                    # Bitwise Trick
                    # ex : 110 -> 6 = 1 << 1 | 1
                    ans += bitset
                else:
                    Queue.append((node.left, bitset))
                    Queue.append((node.right, bitset))

        return ans

#          1
#         / \
#        0   1
#       / \ / \
#      0  1 0  1

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

ans = Solution().sumRootToLeaf(root)
print(ans)