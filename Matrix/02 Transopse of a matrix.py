
def transpose(matrix, r, c):
    temp = matrix
    for i in range(0, r):
        for j in range(i+1, c):
            temp[j][i], matrix[i][j] = matrix[i][j], temp[j][i]

    return temp


res = (transpose(matrix=[[1, 2, 3],
                         [7, 8, 9],
                         [11, 12, 13]], r=3, c=3))
for i in range(0, len(res)):
    print(res[i])
