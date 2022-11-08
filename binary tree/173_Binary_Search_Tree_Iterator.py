# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.BST = self.BSTinorderTree(root)
        self.length = len(self.BST)

    def BSTinorderTree(self, root):
        res = []
        if root:
            res += self.BSTinorderTree(root.left)
            res.append(root.val)
            res += self.BSTinorderTree(root.right)
        return res

    def next(self) -> int:
        # BFS : Queue (FIFO)
        return self.BST.pop(0)

    def hasNext(self) -> bool:
        return len(self.BST) > 0


# Your BSTIterator object will be instantiated and called as such:
#    7 
#   / \
#  3   15
#      / \
#     9   20 

root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
level1_right = root.right
level1_right.left = TreeNode(9)
level1_right.right = TreeNode(20)

obj = BSTIterator(root)
# print(obj.BST)
print(obj.next())     # 3
print(obj.next())     # 7
print(obj.hasNext())  # True
print(obj.next())     # 9
print(obj.hasNext())  # True
print(obj.next())     # 15
print(obj.hasNext())  # True
print(obj.hasNext())  # True
print(obj.next())     # 20
print(obj.hasNext())  # False