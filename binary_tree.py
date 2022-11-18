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

### TODO
# the below function is correct but needs restructuring
# need something cleaner.
# Also Node class must only have initialization 
# and all other tree operations must be left as independant functions or
# methods of another class.
# The setting above is confusing
##
            
def is_subtree(t1, t2):
    def _same_tree(t1, t2):
        if not t1 and not t2:
            return True
            
        if t1 and t2 and t1.value == t2.value:
            return (_same_tree(t1.left, t2.left)) and
                   (_same_tree*t1.right, t2.right))
       
        return False

    if not t2: return True
    if not t1: return False
    if _same_tree(self., t2):
        return True
    return (is_subtree(t1.left, t2) or
            is_subtree(t1.right, t2))

 
tree = Node(5)

tree.insert(7)
tree.insert(4)
tree.subtree_first()
