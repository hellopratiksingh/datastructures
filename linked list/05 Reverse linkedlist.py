class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__ (self):
        self.start = None
    
    def viewList(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next
        
    def insertLast(self, value):
        newNode = Node(value)
        if (self.start == None):
            self.start = newNode    
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        
    def nodeReverse(self):
        prev = None
        curr = self.start
        while curr != None:
            next_= curr.next
            curr.next = prev
            prev = curr
            curr = next_
        self.start = prev
        
mylist = LinkedList()
mylist.insertLast(2)
mylist.insertLast(4)
mylist.insertLast(5)
mylist.insertLast(8)

mylist.nodeReverse()
mylist.viewList()