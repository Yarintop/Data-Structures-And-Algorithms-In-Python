from DataStructures.Trees.BinarySearchTree.BinarySearchTreeNode import BinarySearchTreeNode
import random

class BinarySearchTree:
    def __init__(self, root=None) -> None:
        if isinstance(root, BinarySearchTreeNode):
            self.root = root
        else:
            if root:
                self.root = BinarySearchTreeNode(root)
            else:
                self.root = None
        
    def isEmpty(self):
        return self.root == None
        
    def insert(self, data, root=-1):
        if isinstance(data, BinarySearchTreeNode):
            node = data
        else:
            node = BinarySearchTreeNode(data)
            
        if self.isEmpty():
            self.root = node
        else:
            if root == -1:
                root = self.root
                
            if data <= root.value:
                if root.left == None:
                    root.left = node
                else:
                    self.insert(data, root.left)
            else:
                if root.right == None:
                    root.right = node
                else:
                    self.insert(data, root.right)
                
    def remove(self, data, root=-1):
        if self.isEmpty():
            raise ValueError("Tree is empty.")
        if root == -1:
            root = self.root
        if root == None:
            return None
        
        if data < root.value:
            root.left = self.remove(data, root.left)
        elif data > root.value:
            root.right = self.remove(data, root.right)
        else:
            if not root.left and not root.right: # root is a leaf.
                if self.root == root:
                    self.root = None
                    return self.root
                return None
            if not root.left:
                if self.root == root:
                    self.root = root.right
                return root.right
            elif not root.right:
                if self.root == root:
                    self.root = root.left
                return root.left
            
            temp = root.right
            while temp.left:
                temp = temp.left
                
            root.value = temp.value
            root.right = self.remove(temp.value, root.right)
            
        return root
            
    def search(self, data, node=None):
        if node == None:
            if self.isEmpty():
                return None
            node = self.root
        
        if node.value == data:
            return node
        
        if node.value > data:
            if node.left:
                return self.search(data, node.left)
            return None
        else:
            if node.right:
                return self.search(data, node.right)
            return None
        
    def __str__(self):
        if self.isEmpty():
            return "Tree is Empty."
        s = []
        q = [self.root]
        while len(q):
            t = q.pop(0)
            s.append(t)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return str(s)
    
    
if __name__ == "__main__":
    binaryTree = BinarySearchTree(123)
    binaryTree.insert(543)
    binaryTree.insert(1)
    binaryTree.insert(4)
    binaryTree.insert(765)
    
    print(binaryTree)
    
    n = binaryTree.search(765)
    
    print(n)
    
    binaryTree.remove(123)
    
    print(binaryTree)
    
    b = BinarySearchTree(5)
    print(b)
    b.remove(5)
    print(b)
    