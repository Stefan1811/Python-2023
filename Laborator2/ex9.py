def stadium_seats(matrix):
    rez=[]
    num_rows=len(matrix)
    num_cols=len(matrix[0])
    for row in range(num_rows):
        for col in range(num_cols):
            current_seat=matrix[row][col]
            for roww in range(row+1,num_rows):
                if matrix[roww][col]<=current_seat:
                   rez.append((roww,col))
    return rez

matrix=[
 [1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]] 
rez=stadium_seats(matrix)
print(rez)

#[(2, 2), (3, 4), (2, 4)]