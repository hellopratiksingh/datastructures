class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # insertion at the beginning of the circular linked list
    def insertBeg(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head
    
    # insertion at the end of the circular linked list
    def insertLast(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            
        else:
            self.tail.next = newNode
            newNode.next = self.head
            self.tail = newNode
            
            
    # insertion at specified position in the circular linked list
    def insertAtPos(self, value, pos):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode 
        
     
    # function for displaying the circular linked list
    def display(self):
        if self.head == None:
            print("Linkedlist is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end='-->')
                temp = temp.next
                if temp == self.head:
                    break
    



mynode = CircularLinkedList()
mynode.insertBeg(5)
mynode.insertBeg(10)
mynode.insertBeg(15)
mynode.insertLast(20)
mynode.display()

            

    