# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # using Pre-Order Traversal (NLR) via DFS (stack)
        # TO : O(n+m) where n = Linked List number of node, m = TreeNode number of Node
        # SO : O(3~m) where m = TreeNode Number of Node
        section = ''
        while head:
            section += str(head.val)
            head = head.next
        
        stack = [(root, str(root.val))]
        while stack:
            root, word = stack.pop()
            if root:
                word += str(root.val)
                print(word, section)
                if section in word:
                    return True
                stack.append((root.right, word))
                stack.append((root.left, word))

        return False

        # otherwise approach KMP Algorithm
        # https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N-%2B-L)-Time


# head = [4,2,8]
LN8 = ListNode(6)
LN2 = ListNode(2, LN8)
LN4 = ListNode(4, LN2)
head = ListNode(1, LN4)

# head = [3]
# head = ListNode(2)

# head = [1,10]
# LN10 = ListNode(10)
# head = ListNode(1, LN10)

# root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)

ans = Solution().isSubPath(head, root)
print(ans)
assert ans == True, 'This ans should be True'