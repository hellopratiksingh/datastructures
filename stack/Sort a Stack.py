def sortedInsert(stack, num):
    if len(stack) == 0 or stack[-1] < num:
        stack.append(num)
        return

    n = stack.pop()
    sortedInsert(stack, num)
    stack.append(n) 
    return stack

def sortStack(stack):
    if len(stack) == 0:
        return
    else:
        num = stack.pop()
        sortStack(stack)
        sortedInsert(stack, num)
