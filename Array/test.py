def multiply(num1, num2):
    hashmap = {48:0, 49:1, 50:2, 51:3, 52:4, 53:5, 54:6, 55:7, 56:8, 57:9}
    
    a = 0
    count = 1
    for i in range(len(num1)-1, -1, -1):
        temp = hashmap[ord(num1[i])]
        a = a + (temp * count)
        count *= 10
        
    b = 0
    count = 1
    for i in range(len(num2)-1, -1, -1):
        temp = hashmap[ord(num2[i])]
        b = a + (temp * count)
        count *= 10
        
    return str(a*b)


multiply(num1="123", num2="456")
