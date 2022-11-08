# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # level-order Traversal BFS (Queue)
        Queue = [(root, 1)]
        output ,cur_h, max_val,  = [], 1, root.val
        while Queue:
            node, h = Queue.pop(0)
            if node:
                if h != cur_h:
                    cur_h = h
                    output.append(max_val)
                    max_val = node.val
                else:
                    max_val = node.val if max_val < node.val else max_val
                
                Queue.append((node.left , h+1))
                Queue.append((node.right , h+1))
        
        return output + [max_val] if h != cur_h else output



# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(9)
ans = Solution().largestValues(root)
print(ans)