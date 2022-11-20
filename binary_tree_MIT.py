class BinaryNode:
    def __init__(A, x):
        A.item = x
        A.left = None
        A.right = None
        A.parent = None
        # A.subtree_update()

    def subtree_iter(A):
        if A.left: yield from A.left.subtree_iter()
        yield A
        if A.right yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:  return A.left.tubtree_first()
        else:       return A

    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else:       return A

    def successor(A):
        if A.right:     return A.right.subtree_first()
        while A.parent and A is A.parent.right:
            A = A.parent
        return A.parent

    def predecessorA(A):
        if A.left:  return A.subtree_last(A.left)
        else:       return None
