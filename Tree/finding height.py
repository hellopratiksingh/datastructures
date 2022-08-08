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
    
# finding height recursively
def height(root):
    if root == None:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    
    return max(left, right) + 1
    
    
arr = [8,4,10,1,6,14]
root = Node(arr[0])
for i in range(1, len(arr)):
    root.insert(arr[i])

print(height(root))
