# Definition for a binary tree node.
from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # in-order treversal via DFS (stack)
        # and with BST Delete
        # Time Complexity : O(N logN)
        # Space Complexity : O(N)
        def BSTdelelte(tree, node):
            if tree is None:
                return tree

            if node.val < tree.val:
                if tree.left:
                    tree.left = BSTdelelte(tree.left, node)
                return tree
            if node.val > tree.val: # find right subtree
                if tree.right:
                    tree.right = BSTdelelte(tree.right, node)
                return tree
            
            if tree.right is None:
                return tree.left
            if tree.left is None:
                return tree.right

            aux = tree.right
            while aux.left:
                aux = aux.left
            tree.val = aux.val
            tree.right = BSTdelelte(tree.right, aux.val)
            return tree

        stack = [(root, False)]
        while stack:
            node, traversal = stack.pop()
            if node:
                if traversal:
                    if low > node.val or node.val > high:
                        pre = node.val
                        root = BSTdelelte(root, node)
                        if node.val != pre:
                            stack.append((node.right, False))
                            stack.append((node, True))
                            stack.append((node.left, False))
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return root
        
        # using Solution :
        # Time Complexity : O(n)
        # Space Complexity : O(n)
        def trim(node):
            if node is None:
                return node
            elif node.val > high:
                # 當前結點大🐟 最大邊界值則保留左子樹, 切掉右子樹
                return trim(node.left)
            elif node.val < low:
                # 當前結點小🐟 最小邊界值則保留右子樹, 切掉左子樹
                return trim(node.right)
            else:
                # 在邊界值內則往下搜尋
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)



root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)

ans = Solution().trimBST(root, 1 ,3)
print('=========')
print(ans.val)
if ans.left is not None:
    print(ans.left.val)
if ans.right is not None:
    print(ans.right.val)
if ans.left.right is not None:
    print(ans.left.right.val)
    if ans.left.right.left is not None:
        print(ans.left.right.left.val)


# Wrong Answer 
# [45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]
# 32
# 44

# [45,30,46,10,36,null,49,8,24,34,42,48,null,4,9,14,25,31,35,41,43,47,null,0,6,null,null,11,20,null,28,null,33,null,null,37,null,null,44,null,null,null,1,5,7,null,12,19,21,26,29,32,null,null,38,null,null,null,3,null,null,null,null,null,13,18,null,null,22,null,27,null,null,null,null,null,39,2,null,null,null,15,null,null,23,null,null,null,40,null,null,null,16,null,null,null,null,null,17]
# 32
# 44

# [37,20,49,3,25,41,null,2,12,21,26,38,46,0,null,7,19,null,24,null,35,null,40,43,48,null,1,4,9,17,null,23,null,34,36,39,null,42,44,47,null,null,null,null,6,8,10,14,18,22,null,31,null,null,null,null,null,null,null,null,45,null,null,5,null,null,null,null,11,13,16,null,null,null,null,27,33,null,null,null,null,null,null,null,null,15,null,null,29,32,null,null,null,28,30]
# 41
# 44