def fun(str, s, e):
    if s == e or s > e:
        return True

    if str[s] != str[e]:
        return False
    
    return fun(str, s+1, e-1)


str = "aabaa"
s = 0 
e = len(str)-1
print(fun(str,s,e))