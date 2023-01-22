def createMatrix(block_matrix_size):
    arr = []
    for i in range(block_matrix_size):
        item = []
        for j in range(block_matrix_size):
            item.append(0)
        arr.append(item)
    return arr


def multipy(matrixA, matrixB):
    rows = max(len(matrixA), len(matrixB))
    columns = max(len(matrixA[0]), len(matrixB[0]))

    size = max(rows, columns)
    if size == 1:  # gdy macierz jednoelementowa
        return [[matrixA[0][0] * matrixB[0][0]]]

    matrix_size = newSize(size)

    if min(rows, columns) < matrix_size:
        repairMatrix(matrixA, matrix_size)  # uzupelnienie macierzy zerami
        repairMatrix(matrixB, matrix_size)

    block_matrix_size = matrix_size // 2

    # stworzenie macierzy klatkowych
    matrixA11 = createMatrix(block_matrix_size)
    matrixA12 = createMatrix(block_matrix_size)
    matrixA21 = createMatrix(block_matrix_size)
    matrixA22 = createMatrix(block_matrix_size)
    matrixB11 = createMatrix(block_matrix_size)
    matrixB12 = createMatrix(block_matrix_size)
    matrixB21 = createMatrix(block_matrix_size)
    matrixB22 = createMatrix(block_matrix_size)

    for i in range(block_matrix_size):  # podzielenie macierzy na macierze klatkowe
        for j in range(block_matrix_size):
            matrixA11[i][j] = matrixA[i][j]
            matrixA12[i][j] = matrixA[i][j + block_matrix_size]
            matrixA21[i][j] = matrixA[i + block_matrix_size][j]
            matrixA22[i][j] = matrixA[i + block_matrix_size][j + block_matrix_size]

            matrixB11[i][j] = matrixB[i][j]
            matrixB12[i][j] = matrixB[i][j + block_matrix_size]
            matrixB21[i][j] = matrixB[i + block_matrix_size][j]
            matrixB22[i][j] = matrixB[i + block_matrix_size][j + block_matrix_size]

    # deklaracja i uzupelnianie macierzy obliczeniowych na podstawie: https://pl.wikipedia.org/wiki/Algorytm_Strassena
    operation1 = multipy(addition(matrixA11, matrixA22), addition(matrixB11, matrixB22))
    operation2 = multipy(addition(matrixA21, matrixA22), matrixB11)
    operation3 = multipy(matrixA11, subtraction(matrixB12, matrixB22))
    operation4 = multipy(matrixA22, subtraction(matrixB21, matrixB11))
    operation5 = multipy(addition(matrixA11, matrixA12), matrixB22)
    operation6 = multipy(subtraction(matrixA21, matrixA11), addition(matrixB11, matrixB12))
    operation7 = multipy(subtraction(matrixA12, matrixA22), addition(matrixB21, matrixB22))

    result11 = addition(subtraction(addition(operation1, operation4), operation5), operation7)
    result12 = addition(operation3, operation5)
    result21 = addition(operation2, operation4)
    result22 = addition(addition(subtraction(operation1, operation2), operation3), operation6)

    result_matrix = createMatrix(matrix_size)

    for i in range(block_matrix_size):
        for j in range(block_matrix_size):
            result_matrix[i][j] = result11[i][j]
            result_matrix[i][j + block_matrix_size] = result12[i][j]
            result_matrix[i + block_matrix_size][j] = result21[i][j]
            result_matrix[i + block_matrix_size][j + block_matrix_size] = result22[i][j]

    return result_matrix


def newSize(size):
    n = 0
    while size > 2 ** n:
        n += 1
    return 2 ** n


def repairMatrix(matrix, matrix_size):
    for row in matrix:
        if len(row) < matrix_size:
            for j in range(matrix_size - len(row)):
                row.append(0)

    if len(matrix) < matrix_size:
        temp = matrix_size - len(matrix)
        for i in range(temp):
            matrix.append([0] * matrix_size)


def addition(matrixA, matrixB):
    matrix_size = len(matrixA)
    matrix_result = createMatrix(matrix_size)

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_result[i][j] = matrixA[i][j] + matrixB[i][j]
    return matrix_result


def subtraction(matrixA, matrixB):
    matrix_size = len(matrixA)
    matrix_result = createMatrix(matrix_size)

    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix_result[i][j] = matrixA[i][j] - matrixB[i][j]
    return matrix_result


if __name__ == '__main__':
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    result = multipy(matrix1, matrix2)
    print(result)
