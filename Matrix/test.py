def romanToInt(s):
    data = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = 0
    i = 0
    while i < (len(s)):
        if s[i] == 'I':
            
            if i == len(s)-1:
                res += 1
                i += 1
                
            elif s[i + 1] != 'V' and s[i + 1] != 'X':
                res += data[s[i]]
                i += 1
                
            elif s[i + 1] == "V":
                res += 4
                i += 2
                
            else:
                res += 9
                i += 2
                
        elif s[i] == "V":
            res += 5
            i += 1
                
        elif s[i] == 'X':
            
            if i == len(s)-1:
                res += 10
                i += 1
                
            elif s[i + 1] != 'L' and s[i + 1] != 'C':
                res += data[s[i]]
                i += 1
        
            elif s[i + 1] == "L":
                res += 40
                i += 2
                
            else:
                res += 90
                i += 2
                
        elif s[i] == "L":
            res += 50
            i += 1
            
        elif s[i] == 'C':
            
            if i == len(s)-1:
                res += 100
                i += 1
                
            if s[i + 1] != 'D' and s[i + 1] != 'M':
                res += data[s[i]]
                i += 1

            elif s[i + 1] == "D":
                res += 400
                i += 2

            else:
                res += 900
                i += 2
            
        elif s[i] == "D":
            res += 500
            i += 1
            
        elif s[i] == "M":
            res += 1000
            i += 1
    
    return res

romanToInt("MMMCC")