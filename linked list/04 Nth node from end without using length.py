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
            
    # Print nth node from end of linked list without using length
    def nthNode(self, n):
        if self.start == None:
            return
        elif n <= 0:
            return
        else:
            main = self.start
            ref = self.start
            for i in range(n):
                ref = ref.next

            while ref != None:
                main = main.next
                ref = ref.next
            print(main.data)
            
mylist = LinkedList()
mylist.insertLast(2)
mylist.insertLast(4)
mylist.insertLast(5)
mylist.insertLast(8)

mylist.nthNode(1)