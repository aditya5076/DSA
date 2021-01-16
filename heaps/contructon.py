""" heap is also cnsidered to be the ADT as it is made with 1D-array """
class Heap(object):
    HEAP_SIZE=10
    def __init__(self):
        self.heap=[0]*Heap.HEAP_SIZE #initialize the array with 0*10
        self.currentPosition=-1

    def insert(self,data):
        if(self.is_full()):
            print("Heap is full...")
            return
        self.currentPosition+=1
        self.heap[self.currentPosition]=data
        # to check wether it violates the heap property
        self.fix_up(self.currentPosition)

    def fix_up(self,index):

        """ to get the index of parent node """
        parentIndex=int((index-1)/2) #2*index+1 ---> left child of root node

        """ to check continuously the root node > child nodes """
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parentIndex]
            self.heap[parentIndex]=temp

            # update again untill it becomes 0
            parentIndex= int((index-1)/2)

    def heap_sort(self):
        for i in range(0,self.currentPosition+1):
            temp=self.heap[0]
            print('Node -->',temp)
            self.heap[0]=self.heap[self.currentPosition-i] #rootnode-->lowest node
            self.heap[self.currentPosition-i]=temp #at leaf-->head node
            self.fix_down(0,self.currentPosition-i-1) #as i startswith 0

    def fix_down(self,index,upto):

        while index <= upto:
            left_child_index=2*index+1
            right_child_index=2*index+2

            if left_child_index < upto:
                child_to_swap=None

                if right_child_index>upto:
                    child_to_swap=left_child_index
                else:
                    if self.heap[left_child_index] > self.heap[right_child_index]:
                        child_to_swap=left_child_index
                    else:
                        child_to_swap=right_child_index

                if self.heap[index] < self.heap[child_to_swap]:
                    temp=self.heap[index]
                    self.heap[index]=self.heap[child_to_swap]
                    self.heap[child_to_swap]=temp
                else:
                    break

                index = child_to_swap

            else:
                break



    def is_full(self):
        if self.currentPosition == Heap.HEAP_SIZE:
            return True
        else:
            return False

if __name__ == "__main__":
    heap=Heap()
    heap.insert(10)
    heap.insert(-20)
    heap.insert(0)
    heap.insert(2)
    heap.heap_sort()