class Node(object):
   def __init__(self,data):
        self.data=data
        self.height=0
        self.rightChild=None
        self.leftChild=None

class Avl(object):

    def __init__(self):
        self.root=None
    
    def calculateHeight(self,node):
        if not node: #leaf node
            return -1
        
        return node.height
    
    def insert(self,data):
        self.root=self.insertNode(data,self.root)
    
    def insertNode(self,data,node):
        if not node: #base case
            return Node(data)
        if data < node.data:
            node.leftChild=self.insertNode(data,node.leftChild)
        else:
            node.rightChild=self.insertNode(data,node.rightChild)
        # checj heights param
        """ this was to check max height of left-child and right-child of root node at store it to height variable by adding 1 """
        node.height=max(self.calculateHeight(node.rightChild),self.calculateHeight(node.leftChild))+1

        # setting the violation
        return self.settleViolation(data,node)
    
    def settleViolation(self,data,rootNode):
        balance=self.calculateBalance(rootNode)
        
        """ LEFT-LEFT-HEAVY-SITUATION
                    
        """
        if balance>1 and data<rootNode.leftChild.data:
            print('LEFT-LEFT-HEAVY-SITUATION')
            return self.rotateRight(rootNode)

        """ RIGHT-N1                 N2
                N2       ===       N3       N1
            N3RIGHT-HEAVY-SITUATION
            N1                      N2
                N2       ===    N1      N3
                    N3
        """
        if balance< -1 and data>rootNode.rightChild.data:
            print('RIGHT-RIGHT-HEAVY-SITUATION')
            return self.rotateLeft(rootNode)
        
        """ LEFT-RIGHT-HEAVY-SITUATION
                    N1             N2
                N2       ===   N1      N3
                    N3
        """
        if balance>1 and data > rootNode.leftChild.data:
            print('LEFT-RIGHT-HEAVY-SITUATION')

            rootNode.leftChild=self.rotateLeft(rootNode.leftChild)
            return self.rotateRight(rootNode)

        """ RIGHT-LEFT-HEAVY-SITUATION
            N1                      N2
                N2       ===   N1      N3
            N3        
        """
        if balance< -1 and data < rootNode.rightChild.data:
            print('RIGHT-LEFT-HEAVY-SITUATION')

            rootNode.rightChild=self.rotateRight(rootNode.rightChild)
            return self.rotateLeft(rootNode)
        
        return rootNode
        

    def calculateBalance(self,node):
        if not node:
            return 0

        return self.calculateHeight(node.leftChild)-self.calculateHeight(node.rightChild)
    """ if this returns > 1 : left subtree is heavier than right and have to rotate to right """
    """ if this returns < -1 : right subtree is heavier than left and have to rotate to left """

    def rotateRight(self,node):
        print('rotating right on the rootnode',node.data)

        # swapping the refernece
        tempLeftChild=node.leftChild #store left child of root node
        t=tempLeftChild.rightChild #store right child of that left node of root node
        
        tempLeftChild.rightChild=node
        node.leftChild=t

        """ to check the height parameter """

        # for node
        node.height=max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        # for tempLeftChild
        tempLeftChild.height=max(self.calculateHeight(tempLeftChild.leftChild),self.calculateHeight(tempLeftChild.rightChild))+1

        return tempLeftChild


    def rotateLeft(self,node):
        print('rotating to left on rootnode ',node.data)

        # swapping the refernece
        tempRightChild=node.rightChild #store left child of root node
        t=tempRightChild.leftChild #store right child of that left node of root node
        
        tempRightChild.leftChild=node
        node.rightChild=t

        """ to check the height parameter """

        # for node
        node.height=max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        # for tempRightChild
        tempRightChild.height=max(self.calculateHeight(tempRightChild.leftChild),self.calculateHeight(tempRightChild.rightChild))+1

        return tempRightChild

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    
    def traverseInOrder(self,node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self,data):
        if self.root:
            return self.removeNode(data,self.root)
        
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
        
        if not node:
            return node #if tree had a single value
        
        node.height=max(self.calculateHeight(node.rightChild),self.calculateHeight(node.leftChild))+1

        balance=self.calculateBalance(node)


        if balance>1 and self.calculateBalance(node.leftChild) >= 0:
            print('left left heavy situation')
            return self.rotateRight(node)
        
        if balance>1 and self.calculateBalance(node.leftChild) < 0:
            print('left right heavy situation')
            node.leftChild=self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and self.calculateBalance(node.rightChild) <= 0:
            print('right right heavy situation')
            return self.rotateLeft(node)
        
        if balance>1 and self.calculateBalance(node.rightChild) > 0:
            print(' right left heavy situation')
            node.rightChild=self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node
    
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node






avl=Avl()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)

avl.remove(15)
avl.remove(20)

avl.traverse()


