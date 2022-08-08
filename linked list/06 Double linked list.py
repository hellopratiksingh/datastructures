class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLinkList:
    def __init__(self):
        self.head = None
        
    def insertBeg(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            temp.prev = newNode
            newNode.next = temp
            self.head = newNode
    
    def insertEnd(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
        
    def insertPos(self, value, pos):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            for i in range(1, pos-1):
                temp = temp.next
            newNode.prev = temp
            newNode.next = temp.next
            temp.next.prev = newNode
            temp.next = newNode
    
    def display(self):
        if self.head == None:
            print("Dlink list is Empty")
        
        else:
            temp = self.head
            while temp != None:
                print(temp.data, "-->", end=" ")
                temp = temp.next    
                
    def delBeg(self):
        if self.head == None:
            print("Empty list")
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None
            
    def delEnd(self):
        if self.head == None:
            print("Empty list")
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            
    def delPos(self, pos):
        if self.head == None:
            print("Empty list")
        else:
            temp = self.head.next
            before = self.head
            for i in range(1, pos-1):
                temp = temp.next
                before = before.next
            before.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
                

mylist = DLinkList()
mylist.insertEnd(2)
mylist.insertEnd(3)
mylist.insertEnd(5)
mylist.insertEnd(8)
mylist.display()