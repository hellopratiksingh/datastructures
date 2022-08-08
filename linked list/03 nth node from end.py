class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__ (self):
        self.start = None
        
    def insertLast(self, value):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode    
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            
    # Print nth node from end of linked list    
    def nthNode(self, n):
        len_ = 0
        curr = self.start
        while curr != None:
            len_ += 1
            curr = curr.next
            
        if len_ < n:
            return
        
        pos = (len_- n)+1
        temp = self.start
        for i in range(1, pos):
            temp = temp.next
        print(temp.data)
        
mylist = LinkedList()
mylist.insertLast(10)
mylist.insertLast(5)
mylist.insertLast(15)
mylist.insertLast(20)

mylist.nthNode(n=2)