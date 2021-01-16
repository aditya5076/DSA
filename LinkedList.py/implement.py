class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextnode=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    #O(1)
    def insertStart(self,data):
        self.size+=1

        newNode=Node(data)

        if not self.head:
            self.head=newNode

        else:
            newNode.nextnode=self.head
            self.head=newNode

    # O(1)
    def sizeOfLL(self):
        return self.size

    #O(N)
    def insertEnd(self,data):
        self.size+=1
        
        newNode=Node(data)

        """ TEMPNODE IS REFERENCE TO HEAD NODE """
        tempNode=self.head
        while tempNode.nextnode is not None:
            tempNode=tempNode.nextnode
        tempNode.nextnode=newNode
        newNode.nextnode=None


    #O(N)
    def traverse(self):
        tempNode=self.head
        while tempNode is not None:
            print(tempNode.data)
            tempNode=tempNode.nextnode

    #O(N)
    def remove(self,data):
        self.size-=1

        """ currentnode is reference to head node """
        currentNode=self.head
        previousNode=None

        while currentNode.data != data:
            previousNode=currentNode
            currentNode=currentNode.nextnode
        
        if previousNode is None: #means my currentNode is head node
            self.head=currentNode.nextnode
        
        else:
            previousNode.nextnode=currentNode.nextnode


l=LinkedList()
l.insertStart(45)
l.insertStart(78)
l.insertStart(23) #head node
l.insertEnd(87)

l.remove(87)
l.traverse()
print('size of ll ->',l.sizeOfLL())



""" Qestions """
# 1)to check the ll is in cycle (circular ll)
def check_cycle(node):

    marker1=node
    marker2=node

    while marker2 != None and marker2.nextnode!=None:
        marker1=marker1.nextnode
        marker2=marker2.nextnode.nextnode

        if marker1 == marker2:
            return True
    return False