class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        str = ""
        for i in range(self.rows):
            for j in range(self.cols):
                str += f"{self.get(i,j)} "
            str += '\n'
        return str


    def get(self, i, j):
        if 0 <= i and i < self.rows and 0 <= j and j < self.cols:
            return self.data[i][j]
        else:
            print("[ERROR] Wrong indexes")

    def set(self, i, j, value):
        if 0 <= i and i < self.rows and 0 <= j and j < self.cols:
            self.data[i][j] = value
        else:
            print("[ERROR] Wrong indexes")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            print("[ERROR] The provided matrix cannot be multiplied")
            return
        
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                new_val = 0
                for k in range(self.cols):
                    new_val += self.get(i, k) * other.get(k, j)
                result.set(i, j, new_val)
        return result

    def apply_transform(self, transform_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, transform_func(self.get(i, j)))

matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print(matrix)

t_matrix = matrix.transpose()
print(t_matrix)

matrix2 = Matrix(3, 3)
for i in range(3):
    matrix2.set(i, i, 2)

result = matrix.multiply(matrix2)
print(result)

matrix.apply_transform(lambda x: x * 2)
print(matrix)