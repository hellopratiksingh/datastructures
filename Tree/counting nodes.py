# Counting leaf & non-leaf Nodes

# 1. Leaf 
# if not p.left and p.right

# 2. Node degree 2
# if (p.left and p.right)

# 3. Node degree 1 or 2
# if (p.left or p.right)

# 4. Node degree 1
# if (p.left != None and p.right == None) or (p.left == None and p.right != None)

def allNode(root):
    if root is None:
        return 0
    
    x = allNode(root.left)
    y = allNode(root.right)
    
    return x + y + 1

def leafNodes(root):
    if root is None:
        return 0

    x = allNode(root.left)
    y = allNode(root.right)

    if not root.left and root.right:
        return x + y + 1
    else:
        return x + y

def nodeDeg2(root):
    if root is None:
        return 0

    x = allNode(root.left)
    y = allNode(root.right)

    if root.left and root.right:
        return x + y + 1
    else:
        return x + y

def nodeDeg1or2(root):
    if root is None:
        return 0

    x = allNode(root.left)
    y = allNode(root.right)

    if root.left or root.right:
        return x + y + 1
    else:
        return x + y

def nodedeg1(root):
    if root is None:
        return 0

    x = allNode(root.left)
    y = allNode(root.right)

    if (root.left != None and root.right == None) or (root.left == None and root.right != None):
        return x + y + 1
    else:
        return x + y
