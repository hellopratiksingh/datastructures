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

        
        
if __name__ == '__main__':
    data = [21,28,14,32,25,18,11]
    root = Node(data[0])
    for i in range(1, len(data)):
        root.insert(data[i])
    
    print(root.lvlorder())

