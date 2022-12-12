from binary_tree_MIT import BinaryNode, BinaryTree

def inorderTraversal(A):
    inorder = []
    def inorderIter(A, inorder):
        if not A:
            return None
        inorderIter(A.left, inorder)
        inorder.append(A.item)
        inorderIter(A.right, inorder)
        return None
    inorderIter(A, inorder)
    return inorder


def main():
    tree = BinaryTree()
    tree.build(['F', 'D', 'B', 'E', 'A', 'C'])

    inorder = inorderTraversal(tree.root)
    
    print('Original Tree: ')
    for node in tree:
        print(node)
    
    print('Inorder traversal:')
    for node in inorder:
        print(node)

if __name__ == '__main__':
    main()
