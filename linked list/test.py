class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def insertAtTail(self, cloneHead, cloneTail, data):
        newNode = Node(data, None, None)
        if cloneHead == None:
            cloneHead = newNode
            cloneTail = newNode
            return

        else:
            cloneTail.next = newNode
            cloneTail = newNode
            return 
    def copyRandomList(self, head):

        cloneHead = None
        cloneTail = None
        
        temp = head
        while temp != None:
            self.insertAtTail(cloneHead, cloneTail, temp.val)
            temp = temp.next
        
        arr = []
        temp = head
        while temp != None:
            arr.append(temp.random)
            temp = temp.next
        
        temp = cloneHead
        i = 0
        while temp != None:
            temp.random = arr[i]
            i += 1
            temp = temp.next
            
        return cloneHead
    
obj1 = Solution()
obj1.copyRandomList([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
