from ast import IsNot
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
    def insert(self, data):
        if self.data:
            
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
                    
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)    
                        
        else:
            self.data = data
    
    def inOrder(self):
        ele = []
        
        if self.left:
            ele += self.left.inOrder()
            
        ele.append(self.data)
        
        if self.right:
            ele += self.right.inOrder()
            
        return ele
    
    def iterativeInOrder(self):
        ele = []
        nodeStack = deque()

        if root is None:
            return

        p = root

        while p != None or len(nodeStack) > 0:
            if p != None:
                nodeStack.append(p)
                p = p.left
            else:
                p = nodeStack.pop()
                ele.append(p.data)
                p = p.right

        return ele

    def preOrder(self):
        ele = []
        
        ele.append(self.data)
        
        if self.left:
            ele += self.left.preOrder()
            
        if self.right:
            ele += self.right.preOrder()
            
        return ele
    
    def iterativePreOrder(root):
        ele = []
        nodeStack = deque()
        
        if root is None:
            return
        
        p = root
        
        while p != None or len(nodeStack)>0:
            if p != None:
                ele.append(p.data)
                nodeStack.append(p)
                p = p.left
            else:
                p = nodeStack.pop()
                p = p.right
            
        return ele
            
        
    def postOrder(self):
        ele = []
        
        if self.left:
            ele += self.left.postOrder()
            
        if self.right:
            ele += self.right.postOrder()
            
        ele.append(self.data)
        
        return ele
    
    def lvlorder(root):
        ele = []
        q = deque()
        p = root
        
        ele.append(p.data)
        q.append(p)
        while len(q) > 0:
            p = q.popleft()
            if p.left:
                ele.append(p.left.data)
                q.append(p.left)
                
            if p.right:
                ele.append(p.right.data)
                q.append(p.right)
        
        return ele
    
    def rsearch(self, root, key):
        p = root
        if p is None:
            return False
        elif p.data == key:
            return p.data
        elif key < p.data:
            return self.rsearch(p.left, key)
        else:
            return self.rsearch(p.right, key)      
        
    def itrsearch(self, root, key):
        p = root
        
        while p is not None:
            if key == p.data:
                return p.data
            
            elif key < p.data:
                p = p.left
                
            else:
                p = p.right 
                
        return False     
    
    def insertnode(self, key):
        p = root
        r = None
        while p is not None:
            if key == p.data:
                return p.data

            elif key < p.data:
                r = p
                p = p.left

            else:
                r = p
                p = p.right
                
        p = Node(key)
        if p.data < r.data:
            r.left = p
        else:
            r.right = p
             
        
if __name__ == '__main__':
    data = [21,28,14,32,25,18,11]
    root = Node(data[0])
    for i in range(1, len(data)):
        root.insert(data[i])
    
    print(root.inOrder())
    root.insertnode(33)
    print(root.inOrder())


