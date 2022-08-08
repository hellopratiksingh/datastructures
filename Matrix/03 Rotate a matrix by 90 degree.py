
def rotate(mat, r, c):
    n = len(mat)
    for i in range(n):
        for j in range(0, i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n):
        j = n-1
        k = 0
        while k < j:
            mat[i][k], mat[i][j] = mat[i][j], mat[i][k]
            k += 1
            j -= 1

    return mat



res = (rotate(mat=[
    [1, 2, 3],
    [4,5,6],
    [7, 8, 9],
], r=3, c=3))

for i in range(0, len(res)):
    print(res[i])
