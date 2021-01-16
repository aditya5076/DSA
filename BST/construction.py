""" if BST is balanced the TC->O(logN) on every operations else TC->O(N)
    for that we can use RBT and AVL tree known as balanced binary tree BBT
"""

class Node(object):
    def __init__(self,data):
        self.data=data
        self.rightChild=None
        self.leftChild=None

class BST(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        # for left
        if data<node.data:
            # check that left child exist
            if node.leftChild:
                self.insertNode(data,node.leftChild) #process recursive

            else:
                node.leftChild=Node(data) #insert node
        # for right
        else:

            # check that right child exist
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild=Node(data)

    """ remove """

    def removeNode(self,data,node):
        if not node:
            return node

        if data<node.data: #remove left child
            node.leftChild=self.removeNode(data,node.leftChild)
        elif data>node.data:  #remove right child
            node.rightChild=self.removeNode(data,node.rightChild)
        else:

            if not node.leftChild and node.rightChild: #is a leaf node
                print('removing leaf node...')
                del node
                return None

            """ having a single child """
            if not node.leftChild:
                print('removing node with single right child')
                tempNode=node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('removing node with single left child')
                tempNode=node.leftChild
                del node
                return tempNode

            print('removing node having two childrens')
            tempNode=self.getPredecessor(node.leftChild) #tempNode will store greatest value in left-part
            node.data=tempNode.data #swapping the data
            node.leftChild=self.removeNode(tempNode.data,node.leftChild)
        return node




    """ getPredecessor is a greatest right-child node in left-most part of parent-node """
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node






    def remove(self,data):
        if self.root:
            self.root=self.removeNode(data,self.root)

    """ TRAVERSE MINMAX """
    # get min value
    def getMinVal(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    # get max value
    def getMaxVal(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    """ TRAVERSE INORDER """
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)
        # print(node.data)



# testing
bst=BST()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

# print(bst.getMinVal())
# print(bst.getMaxVal())


bst.remove(5)
bst.traverse()
