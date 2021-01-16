class Stack(object):
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1] #returns last item of [index]

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


s=Stack()

# print(s.isEmpty())

s.push(4)
s.push('aditya')
s.push(True)


print(s.pop())
# print(s.pop())

print(s.peek())

print(s.show())