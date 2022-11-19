class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


class BinaryTree:
    def __init__(self, rootNode):
        self.root = rootNode

    
    def insert(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

    #@staticmethod
    def is_subtree(self, t1, t2):
        def _same_tree(t1, t2):
            if not t1 and not t2:
                return True
   
            if t1 and t2 and t1.value == t2.value:
                return (_same_tree(t1.left, t2.left) and
                       _same_tree(t1.right, t2.right))
   
            return False
   
        if not t2: return True
        if not t1: return False
        if _same_tree(t1, t2):
            return True
        return (self.is_subtree(t1.left, t2) or
                self.is_subtree(t1.right, t2))
   
    #@staticmethod
    def subtree_first(self, node):
        if node.left is None:
            return node
        self.subtree_first(node.left)
        
    def subtree_insert_after(self, node, new):
        if not node.right:
            node.right = new
        else:
            successor = self.subtree_first(node.right)
            successor.left = new

rootNode = Node(4)
tree = BinaryTree(rootNode)
testNode = Node(7)
tree.insert(tree.root, testNode)
#tree.insert(tree.root, Node(6))
tree.insert(tree.root, Node(6))
tree.subtree_insert_after(testNode, Node(5))
