def sayDigit(n, arr):
    if n == 0:
        return
    
    else:
        sayDigit(n//10, arr)
        print(arr[n%10], end=" ")
    
    
arr = ["zero", "one", "two", "three",
        "four", "five", "six","seven","eight", "nine"]
n = 1001
sayDigit(n, arr)