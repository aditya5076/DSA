class Deque(object):

    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        self.items.append(item)
    
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeLast(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)


d=Deque()

d.addRear('world')
d.addFront('hello')
# d.show()

print(d.removeFront() + ' ' + d.removeLast())
    
