class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        
    def insert(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
                
    def subtree_first(self):
        if self.left:
            self.left.subtree_first()
        else:
            return self
            
    def subtree_insert_after(self, x):
        assert x >= self.value
    
tree = Node(5)

tree.insert(7)
tree.insert(4)
tree.subtree_first()
