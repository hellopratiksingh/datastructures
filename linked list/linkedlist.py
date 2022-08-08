class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.start = None
        
        
    def viewList(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next                
        
        
    def insertBeg(self, value):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode
        else:
            newNode.next = self.start
            self.start = newNode       
        
                
    def insertLast(self, value):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode    
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    
    
    def insertAtPos(self, value, pos):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode
        else: 
            temp = self.start
            for i in range(pos-1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            
            
    def delFirst(self):
        if self.start == None:
            print("Linkedlist is Empty")
        else:
            self.start = self.start.next    
            
        
    def delEnd(self):
        temp = self.start.next
        prev = self.start
        while temp.next != None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        
        
    def delNode(self, pos):
        temp = self.start.next
        prev = self.start
        for i in range(1, pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None            
        
        
            
            
mylist = LinkedList()

mylist.insertLast(10)
mylist.insertLast(20)
mylist.insertLast(30)
mylist.insertLast(40)
mylist.viewList()
