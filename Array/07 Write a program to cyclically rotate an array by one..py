# Write a program to cyclically rotate an array by one.
# 1
def rotate(a, n):
    i = n-1
    for i in range(n-1, 0, -1):
        a[i], a[i-1] = a[i-1], a[i]

    return a


#2
def rot(a, n):
    temp = a[n-1]
    i = n-1
    while i >= 0:
        if i == 0:
            a[i] = temp
        else:
            a[i] = a[i-1]
        i -= 1
    print(a)

