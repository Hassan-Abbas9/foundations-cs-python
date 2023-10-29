def add_matrices():
    rows = int(input("Enter the number of rows:  "))
    columns = int(input("Enter the number of Columns:  "))
    matrixA = []
    matrixB = []
    for i in range(rows):
        input_strings = input(f"Enter elements of the {i + 1} row of the first matrix: ").split()
        numbers = []
        for j in range(columns):
            numbers.append(int(input_strings[j]))
        matrixA.append(numbers)

    for i in range(rows):
        input_strings = input(f"Enter elements of the {i + 1} row of the second matrix: ").split()
        numbers = []
        for j in range(columns):
            numbers.append(int(input_strings[j]))
        matrixB.append(numbers)

    result_matrix = matrixA.copy()
    for i in range(rows):
        for j in range(columns):
            result_matrix[i][j] = matrixA[i][j] + matrixB[i][j]

    print(f'The sum is: {result_matrix}')


add_matrices()
