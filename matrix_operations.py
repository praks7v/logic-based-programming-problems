def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

    # result = []
    # for i in range(len(matrix1)):
    #     row = []
    #     for j in range(len(matrix1[0])):
    #         row.append(matrix1[i][j] + matrix2[i][j])
    #     result.append(row)
    # return result


def subtract_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

    # result = []
    # for i in range(len(matrix1)):
    #     row = []
    #     for j in range(len(matrix1[0])):
    #         row.append(matrix1[i][j] - matrix2[i][j])
    #     result.append(row)
    # return result


def multiply_matrices(matrix1, matrix2):
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in
              range(len(matrix1))]
    return result

    # result = []
    # for i in range(len(matrix1)):
    #     row = []
    #     for j in range(len(matrix2[0])):
    #         element_sum = 0
    #         for k in range(len(matrix2)):
    #             element_sum += matrix1[i][k] * matrix2[k][j]
    #         row.append(element_sum)
    #     result.append(row)
    # return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    matrix_A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    print("Matrix A:")
    print_matrix(matrix_A)

    print("\nMatrix B:")
    print_matrix(matrix_B)

    # Addition
    result_addition = add_matrices(matrix_A, matrix_B)
    print("\nMatrix A + B:")
    print_matrix(result_addition)

    # Subtraction
    result_subtraction = subtract_matrices(matrix_A, matrix_B)
    print("\nMatrix A - B:")
    print_matrix(result_subtraction)

    # Multiplication
    result_multiplication = multiply_matrices(matrix_A, matrix_B)
    print("\nMatrix A * B:")
    print_matrix(result_multiplication)
