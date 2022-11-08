# Definition for a binary tree node.
from contextlib import nullcontext
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # using DFS (stack) to handle
        stack = [(root)]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)

        return root

    def Marris_Algorithm(self, root):
        cur = root
        sum = 0
        while cur:
            if cur.right:
                leftMost = cur.right
                while leftMost.left:
                    leftMost = leftMost.left
                
                if leftMost.left: 
                    leftMost.left = cur
                    cur = cur.right
                else:
                    leftMost.left = None
                    cur = cur.left
            else:
                cur = cur.left
        return root

    def inverse_inorderTraversal(self, node):
        res = []
        sum = 0
        stack = [(node, False, 0)]
        while stack:
            node, travered, notation = stack.pop()
            
            if travered:
                if notation in ('R', 'N'):
                    sum += node.val
                else:
                    sum -= node.val
                node.val = sum
                res.append(node.val)
            else:
                if node:
                    stack.append((node.left, False , 'L'))
                    stack.append((node, True , 'N'))
                    stack.append((node.right, False, 'R'))
        return res

    # def inverse_inorder_BFS_recursion(self, node, stack=[]):
    #     if not stack:
    #         return []
    #     node, travered = stack.pop()
    #     if travered:
    #         res.append(node.val)
    #     else:
    #         if node:
    #             self.inverse_inorder_BFS_recursion(node.left, stack)
    #             self.inverse_inorder_BFS_recursion(node, stack)
    #             self.inverse_inorder_BFS_recursion(node.right, stack)
    #     return res

    def postOrderTraversl(self, node):
        res = []
        if node:
            res += self.postOrderTraversl(node.left)
            res += self.postOrderTraversl(node.right)
            res.append(node.val)
        return res
   
    

    def inverse_inorderTraversal2(self, node):
        res = []
        if node:
            res += self.inverse_inorderTraversal2(node.right)
            res.append(node.val)
            res += self.inverse_inorderTraversal2(node.left)
            # res.append((node.left.val if node.left else 0 ) + (node.right.val if node.right else 0 ) + node.val)
            
        return res

    def sumNode(self):
        pass


#         4 
#        / \
#       1   6
#      / \  / \
#     0  2  5  7 
#         \     \
#          3     8
root = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))


# print(Solution().inverse_inorderTraversal(root))

print(Solution().postOrderTraversl(root))
# print(Solution().Marris_Algorithm(root))
# print(Solution().inverse_inorderTraversal2(root))
root = TreeNode(4, TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))), TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
res = Solution().bstToGst(root)
print(res.val) # 30
print(res.left.val) # 36
print(res.right.val) # 21
print(res.left.left.val) # 36
print(res.left.right.val) # 35
print(res.left.right.right.val) # 33
print(res.right.left.val) # 26
print(res.right.right.val) # 15
print(res.right.right.right.val) # 8
