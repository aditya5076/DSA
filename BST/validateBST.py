class Node(object):
    def __init__(self,data):
        self.data=data
        self.rightChild=None
        self.leftChild=None

class BST(object):
    INT_MIN=-4294967296
    INT_MAX=4294967296
    def __init__(self):
        self.root_node=None

    def bst(self,root):
        return self.validate_bst(root,BST.INT_MIN,BST.INT_MAX)

    def validate_bst(self,root_node,mini,maxi):
        if root_node is None:
            return True

        if root_node.data < mini or root_node.data > maxi:
            return False

        return self.validate_bst(root_node.leftChild,mini,root_node.data-1) and  self.validate_bst(root_node.rightChild,root_node.data+1,maxi)

