 
def snake(matrix, n):
    for i in range(0, n):
        if i % 2 == 0:
            for j in range(0, n):
                print(str(matrix[i][j]),
                        end=" ")
            
        else:
            for j in range(n-1, -1, -1):
                print(str(matrix[i][j]),
                        end= " ")


snake(matrix=[[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]], n=4)
