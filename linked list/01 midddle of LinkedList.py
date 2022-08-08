import math

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
            
    def viewList(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next  
        
    def middle(self):
        count = -1
        temp = self.start
        temp2 = self.start
        while temp != None:
            temp = temp.next
            count += 1
        middle = math.ceil(count / 2)
        for i in range(middle):
            temp2 = temp2.next
        while temp2 != None:
            print(temp2.data, end=" ")
            temp2 = temp2.next
        
            
    
mylist = LinkedList()

mylist.insertLast(1)
mylist.insertLast(2)
mylist.insertLast(3)
mylist.insertLast(4)
mylist.insertLast(5)
mylist.insertLast(6)

mylist.middle()

    
