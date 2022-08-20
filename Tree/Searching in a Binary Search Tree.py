#Recursive Searching in a Binary Search Tree

def rsearch(root, key):
    p = root
    if p is None:
        return ("Not Found")
    elif p.data == key:
        return p.data
    elif key < p.data:
        return rsearch(p.left, key)
    else:
        return rsearch(p.right, key)
    
#iterative Searching in a Binary Search Tree
def itrsearch(root, key):
    p = root

    while p is not None:
        if key == p.data:
            return p.data

        elif key < p.data:
            p = p.left

        else:
            p = p.right

    return False
        
    

