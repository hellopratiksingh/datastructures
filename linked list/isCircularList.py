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


    def isCircularList(self):
        if self.start == None:
            return False
        
        else:
            temp = self.start.next
            while temp != None and temp != self.head:
                temp = temp.next
            
            if temp == self.head:
                return True
            return False


    def detectLoop(self):
        if self.start == None:
            return False
        
        else:
            temp = self.start.next
            while temp != None and temp != self.head:
                temp = temp.next
            
            if temp == self.head:
                return True
            return False
        
    # function for detecting the loop in the linked list
    def floydDetectLoop(self):
        if self.start == None:
            return False
        
        else:
            slow = self.start
            fast = self.start
            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False