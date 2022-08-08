from collections import deque

def pushAtBottom(myStack: deque, x: int):
	if len(myStack) == 0:
		myStack.append(x)
		return

	else:
		z = myStack.pop()
		pushAtBottom(myStack, x)
		myStack.append(z)
		return myStack


print(pushAtBottom([7, 1, 4, 5], 9))
