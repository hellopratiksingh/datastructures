def sod(n: int) -> int:
    if n < 10:
        return n
    
    else:
        return sod(n//10) + n%10
        
print(sod(9987))