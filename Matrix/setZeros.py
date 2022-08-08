def setZeroes(matrix):
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i not in row:
                    row.append(i)
                if j not in col:
                    col.append(j)

    for r in row:
        matrix[r] = [0 for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j in col:
                matrix[i][j] = 0

    return matrix

setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])