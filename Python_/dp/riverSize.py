
def riverSize(matrix):
    row, col = len(matrix), len(matrix[0])
    visited = set()
    result = []

    def getSize(i, j):
        if i < 0 or j < 0 or j >= col or i >= row or (i, j) in visited or matrix[i][j] != 1:
            return 0
        visited.add((i, j))

        return 1 + getSize(i-1, j) + getSize(i+1, j) + \
            getSize(i, j-1) + getSize(i, j+1)

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                size = getSize(i, j)
                if size != 0:
                    result.append(size)

    return (result)


matrix = [[0, 0, 0, 1, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 1, 1],
          [1, 0, 0, 1, 0]]

print(
    riverSize(matrix)
)
