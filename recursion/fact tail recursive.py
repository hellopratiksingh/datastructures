def fun(n, k=1):
    if n == 0:
        return k
    else:
        return fun(n-1, k*n)


print(fun(5))
