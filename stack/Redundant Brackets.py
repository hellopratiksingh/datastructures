from collections import deque


def findRedundantBrackets(s):
	stack = deque()
	for c in s:
		if c == "(" or c == "+" or c == "-" or c == "*" or c == "/":
			stack.append(c)
   
		else:
			if c == ")":
				flag = True
    
				while stack[-1] != "(":
					top = stack[-1]
					if top == "+" or top == "-" or top == "*" or top == "/":
						flag = False
					stack.pop()

				if flag == True:
					return True
				stack.pop()
	return False


findRedundantBrackets("(a+c*b)+(c))")
