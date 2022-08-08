from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
         
    def insertIntoBst(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insertIntoBst(data)
            else:
                self.left = Node(data)

        else:
            if self.right:
                self.right.insertIntoBst(data)
            else:
                self.right = Node(data)
                
    
    def preOrder(self):
        ele = []
        
        # visit base Node
        ele.append(self.data)
        
        # visit left subtree
        if self.left:
            ele += self.left.preOrder()
            
        # visit right subtree
        if self.right:
            ele += self.right.preOrder()
            
        return ele
    
    
    def in_order_traversal(self):
        ele = []
        
        # visit left subtree
        if self.left:
            ele += self.left.in_order_traversal()
        
        # visit base Node
        ele.append(self.data)
        
        # visit right subtree
        if self.right:
            ele += self.right.in_order_traversal()
        
        return ele
    
    
    def postOrder(self):
        ele = []
        
        # visit left subtree
        if self.left:    
            ele += self.left.postOrder()
        
        # visit right subtree
        if self.right:
            ele += self.right.postOrder()
        
        # visit base Node
        ele.append(self.data)
         
        return ele
    
    
    def levelOrder(self):
        if self.data is None:
            return
        ele = []
        
        q = deque()
 
        # Enqueue Root and initialize height
        q.append(self)
 
        while(len(q) != 0):
    
            # Print front of queue and
            # remove it from queue
            ele.append(q[0].data)
            node = q.popleft()

            # Enqueue left child
            if node.left is not None:
                q.append(node.left)
    
            # Enqueue right child
            if node.right is not None:
                q.append(node.right)
        return ele
        
    def search_tree(self, val):
        if val == self.data:
            return True
        
        if val < self.data:
            # element might be in left subtree
            if self.left:
                return self.left.search_tree(val)
            else:
                return False    
        
        if val > self.data:
            if self.right:
                return self.right.search_tree(val)
            else:
                return False
        
    def countNode(self):
        if self.data == None:
            return 0
        
        x, y = 0, 0
        if self.left:
            x = self.left.countNode()
            
        if self.right:
            y = self.right.countNode()
        
        return x + y + 1
    
    
    def minValue(self):
        temp = self
        while temp.left != None:
            temp = temp.left
        return temp.data
    
    
    def maxValue(self):
        temp = self
        while temp.right != None:
            temp = temp.right
        return temp.data
    
    
    def deleteNode(self, val):
        if self.data == val:
            if self.right == None:
                return self.left
            elif self.left == None:
                return self.right
            else:
                self.data = self.right.minValue()
                self.right.deleteNode(self.data)
                
        elif val < self.data:
            self.left = self.left.deleteNode(val)
        else:
            self.right = self.right.deleteNode(val)
            
        return self
    
    
def buildTree(elements):
    root = Node(elements[0])
    
    for i in range(1, len(elements)):
        root.insertIntoBst(elements[i])
        
    return root
    

if __name__ == '__main__':
    nums = [10,5,12,14,20,8,4,2,18]
    tree = buildTree(nums)
    print(tree.in_order_traversal()) 
    # print(tree.postOrder())
    print(tree.deleteNode(8))
    print(tree.in_order_traversal())
    
       