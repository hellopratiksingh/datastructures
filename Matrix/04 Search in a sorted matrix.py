def search(matrix, r, c, num):
    res = ()
    for i in range(0, r):
        for j in range(c-1, -1, -1):
            if matrix[i][j] == num:
                res = (i,j)
                return res 
            elif matrix[i][j] >= num:
                j -= 1

            elif matrix[i][j] <= num:
                i += 1
    return -1


print(search(matrix=[
    [10,20,30,40],
    [15,25,35,80],
    [90,45,80,100]
],r=3,c=3,num=45))
