# BST
class BinarySearchTree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if not self.data:
            self.data == data
            return
        
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left = self.left.insert(data)
            self.left = BinarySearchTree(data)
            return 

        if data > self.data:
            if self.right:
                self.right = self.right.insert(data)
            self.right = BinarySearchTree(data)
            return 
        
    def delete(self, data):
        # LeetCode 450. Delete Node in a BST
        if self == None:
            return self

        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            return self
        
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            return self

        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        aux = self.right
        while aux.left:
            aux = aux.left
        self.data = aux.data
        self.right = self.right.delete(aux.data)
        return self

    def preOrderTraversal(self, root):
        # LeetCode 144. Binary Tree Preorder Traversal 
        # PreOrder Traversal : NLR
        res = []
        if root:
            res.append(root.data)
            res += self.preOrderTraversal(self.left)
            res += self.preOrderTraversal(self.right)
        return res
        # clearn code
        return [root.val] + \
            self.preorderTraversal(root.left) + \
            self.preorderTraversal(root.right) if root else []
    
    def inOrderTraversal(self, root):
        # LeetCode 94. Binary Tree InOrder Traversal
        # Inorder Traversal : LNR
        # here using Recursive 
        # and also using stack
        res = []
        if root:
            res += self.inOrderTraversal(self.left)
            res.append(root.data)
            res += self.inOrderTraversal(self.right)
        return res
        # here is DFS (stack)
        # Suggested Read :
        # https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions
        res, stack = [], [(root, False)]
        while stack:
            root, visited = stack.pop()
            if root:
                if visited:
                    res.append(root.val)
                else:
                    stack.append((root.right), False)
                    stack.append((root), True)
                    stack.append((root.left), False)
        return res

    def inOrderTraversal_MorrisAlgorithm(self, root):
    #https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/668448/Morris-Traversal
        
        def findPredecessor(root):
            cur = root.left
            while cur.right and cur.right != root:
                cur = cur.right
            return cur

        res = []
        while root:
            # print(f' c : {root and root.val} ')
            if not root.left:  # no left subtree
                # print(f'input res : {root.val}')
                res.append(root.val)
                root = root.right
            else:
                pred = findPredecessor(root)
                # print(f' pred : {pred and pred.val} ')
                if pred.right != root:
                    pred.right = root
                    root = root.left
                else:
                    root.left = None
        return res
    

    def postOrderTraversl(self, root):
        # LeetCode 145. Binary Tree Postorder Traversal
        res = []
        if root:
            res += self.postOrderTraversl(self.left)
            res += self.postOrderTraversl(self.right)
            res.append(root.data)
        return res
        # BST postorderTraversal : LRN
        res = []
        stack = [(root, False)]
        while stack:
            root, travered = stack.pop()
            if travered:
                res.append(root.val)
            else:
                if root:
                    stack.append((root, True))
                    stack.append((root.right, False))
                    stack.append((root.left, False))    
                
        return res
        # Morris Algorithm 
        # https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/1930210/Python-Functional-or-Stack-or-Morris-Traversal-Multiple-Solutions!

    def search(self, data):
        if self.data:
            return False
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            return False
        
        if data > self.data:
            if self.right:
                return self.right.search(data)
            return False
        
        if data == self.data:
            return True
