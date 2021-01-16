""" Tries have has many numbers of children has many size of alphabet, but thts not the case in TST has it has three child-nodes """

class Node(object):
    def __init__(self,character):
        self.character=character
        self.leftNode=None
        self.rightNode=None
        self.middleNode=None
        self.value=0

class TST(object):
    def __init__(self):
        self.rootNode=None

    def put(self,key,value): #eg-->('cat',89)
        self.rootNode=self.put_item(self.rootNode,key,value,0)

    def put_item(self,node,key,value,index):

        char=key[index]

        if node == None:
            node=Node(char)

        if char < node.character:
            node.leftNode=self.put_item(node.leftNode,key,value,index)
        elif char > node.character:
            node.rightNode=self.put_item(node.rightNode,key,value,index)
        elif index < len(key) - 1: #index reached to last char of key
            node.middleNode=self.put_item(node.middleNode,key,value,index+1)
        else:
            node.value=value

        return node

    def get(self,key):

        node=self.get_item(self.rootNode,key,0)

        if node==None:
            return -1

        return node.value

    def get_item(self,node,key,index):

        if node == None:
            return None

        char=key[index]

        if char < node.character:
            return self.get_item(node.leftNode,key,index)
        elif char > node.character:
            return self.get_item(node.rightNode,key,index)
        elif index < len(key) - 1: #index reached to last char of key
            return self.get_item(node.middleNode,key,index+1)
        else:
            return node

if __name__ == "__main__":
    tst=TST()

    tst.put('apple',67)
    tst.put('cat',70)

    print(tst.get('apple'))
    print(tst.get('banana'))


