# Definition for a binary tree node.

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Level Treversal in BFS (queue)
        h, sum, max_level, max_level_val  = 1, 0, 1, root.val
        queue = [(root, 1)]
        # res = []
        while queue:
            node, node_h = queue.pop(0)

            if node:
                if node_h != h:
                    h = node_h
                    if max_level_val < sum:
                        max_level = h - 1
                        max_level_val = sum
                    sum = node.val
                    # res.append((h, sum, 'change', max_level, max_level_val))
                else:
                    sum += node.val
                    # res.append((h, sum, 'same', max_level, max_level_val))
                queue.append((node.left, h+1))
                queue.append((node.right, h+1))

        if max_level_val < sum:
            max_level = h
            # max_level_val = sum
            # res.append((h, sum, 'last', max_level, max_level_val))
        return max_level
        # return res
            
root = TreeNode(-100)
root.left = TreeNode(7)
root.right = TreeNode(2)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

ans = Solution().maxLevelSum(root)
print(ans)



