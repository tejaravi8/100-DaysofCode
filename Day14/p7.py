# 7. Transpose Matrix
def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

print(transpose([[1, 2, 3], [4, 5, 6]]))