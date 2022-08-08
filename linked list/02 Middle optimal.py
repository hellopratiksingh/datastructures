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
        if self.start == None:
            print("linked list is empty")
            return
        else:
            count = 0
            curr = self.start
            mid = self.start
            while curr != None:
                if count % 2 != 0:
                    mid = mid.next
                count += 1
                curr = curr.next
            print(mid.data)
                         
mylist = LinkedList()
mylist.insertLast(2)
mylist.insertLast(5)
mylist.insertLast(6)
mylist.insertLast(8)
mylist.insertLast(10)
mylist.insertLast(15)
mylist.insertLast(18)

mylist.middle()