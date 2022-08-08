def insertAtBottom(stack, x):
    if len(stack) == 0:
        stack.append(x)
        return
    else:
        z = stack.pop()
        insertAtBottom(stack, x)
        stack.append(z)
        return stack

def reverseStack(stack) :
    if len(stack) == 0:
        return
    else:
        temp = stack.pop()
        reverseStack(stack)
        insertAtBottom(stack, temp)