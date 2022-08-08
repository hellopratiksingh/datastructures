class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        
    # Funtion for viewing Queue
    def viewQueue(self):
        if self.front == None:
            print("list is empty")
        else:
            temp = self.front
            while temp != None:
                print(temp.data,"<--", end=' ')
                temp = temp.next
    
    # Addition of elements from back
    def enqueue(self, value):
        newNode = Node(value)
        if self.front == None:
            self.front = newNode
        else:
            self.back.next = newNode
        self.back = newNode
        
    # Deletion of elements from front
    def dequeue(self):
        if self.front == None:
            print("queue is empty")
        else:
            x = self.front.data
            self.front = self.front.next
            return x
        
myque = Queue()
myque.enqueue(5)       
myque.enqueue(7)
myque.enqueue(8)
myque.enqueue(10)
myque.dequeue()
myque.viewQueue()