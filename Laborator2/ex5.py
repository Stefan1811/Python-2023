def under_main_diag(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i>j:
                matrix[i][j]=0
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix=under_main_diag(matrix)
for i in matrix:
    print(i)