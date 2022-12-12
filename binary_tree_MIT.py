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
        if A.right: yield from A.right.subtree_iter()

    def subtree_first(A):
        if A.left:  return A.left.subtree_first()
        else:       return A

    def subtree_last(A):
        if A.right: return A.right.subtree_last()
        else:       return A

    def successor(A):
        if A.right:     return A.right.subtree_first()
        while A.parent and A is A.parent.right:
            A = A.parent
        return A.parent

    def predecessor(A):
        if A.left:  return A.left.subtree_last()
        while A.parent and A is A.parent.left:
            A = A.parent
        return A.parent

    def subtree_insert_before(A, B):
        if A.left:
            A = A.left.subtree_last()
            A.right, B.paretnt = B, A

        else:
            A.left, B.parent = B, A
    
    def subtree_insert_after(A, B):
        if A.right:
            A = A.right.subtree_first()
            A.left, B.parent = B, A
        else:
            A.right, B.parent = B, A

    def subtree_delete(A):
        if A.left or A.right:
            if A.left: B = A.predecessor()
            else: B = A.successor()
            A.item, B.item = B.item, A.item
            return B.subtree_delete()
        if A.parent:
            if A.parent.left is A: A.parent.left = None
            else: A.parent.right = None

        return A

class BinaryTree:
    def __init__(T, Node_Type = BinaryNode):
        T.root = None
        T.size = 0
        T.Node_Type = Node_Type
    def __len__(T):
        return T.size
    def __iter__(T):
        for A in T.root.subtree_iter():
            yield A.item

    def build(T, A):
        def build_subtree(A, i, j):
            n = (i + j) // 2
            root = BinaryNode(A[n])
            if i < n:
                root.left = build_subtree(A, i, n - 1)
                root.left.parent = root
            if j > n:
                root.right = build_subtree(A, n + 1, j)
                root.right.parent = root
            return root
        T.root = build_subtree(A, 0, len(A) - 1)

    def tree_iter(T):
        if T.root:
            node = T.root.subtree_first()
            while node:
                yield node
                node = node.successor()

class BSTNode(BinaryNode):
    def subtree_find(A, k):
        if k < A.item.key:
            A.left.subtree_find(k)
        elif k > A.item.key:
            A.right.subtree_find(k)
        else:
            return A.item()


#Tree = BinaryTree()
#Tree.build(['F', 'D', 'B', 'E', 'A', 'C'])
#for node in Tree.tree_iter():
#    print(node.item)


