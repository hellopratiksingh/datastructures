from collections import deque


def findMinimumCost(str):
	if len(str) % 2 == 1:
		return -1
	stack = deque()
	for i in str:
		if i == "{":
			stack.append("{")

		else:
			if len(stack) != 0 and stack[-1] == "{":
				stack.pop()
			else:
				stack.append(i)

	# now stack contains only invalid paranthesis
	a, b = 0, 0
	while len(stack) != 0:
		if stack[-1] == "{":
			b += 1
		else:
			a += 1
		stack.pop()
	res = (a+1)//2 + (b+1)//2
	return abs(res)
