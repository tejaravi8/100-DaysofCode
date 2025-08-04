# 3. Rotate Matrix 90 degrees Clockwise
def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)-1, -1, -1):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))