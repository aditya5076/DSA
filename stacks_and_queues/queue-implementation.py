class Queue(object):
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item) #will add item at first as index is 0

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)

q=Queue()

# print(q.isEmpty())

q.enqueue(10)
q.enqueue('aditya')
q.enqueue(False)

q.dequeue()

print(q.size())

q.show()

