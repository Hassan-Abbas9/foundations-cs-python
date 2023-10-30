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


# add_matrices()

def rotation_matrix():
    rows = int(input("Enter the number of rows for the first matrix"))
    columns = int(input("Enter the number of columns for the first matrix"))
    matrix_x = []
    for i in range(rows):
        input_strings = input(f"Enter the elements of the row {i + 1} of the first matrix: ").split()
        numbers = []
        for j in range(columns):
            numbers.append(int(input_strings[j]))
        matrix_x.append(numbers)
    print(matrix_x)

    rows2 = int(input("Enter the number of rows for the second matrix"))
    columns2 = int(input("Enter the number of columns for the second matrix"))
    matrix_y = []
    for i in range(rows2):
        input_strings = input(f"Enter the elements of the row {i + 1} of the second matrix: ").split()
        numbers = []
        for j in range(columns2):
            numbers.append(int(input_strings[j]))
        matrix_y.append(numbers)
    print(matrix_y)

    if len(matrix_x[0]) != len(matrix_y) or len(matrix_x) != len(matrix_y[0]):
        print(f"the length of matrix_x[0] is:   {len(matrix_x[0])}")
        print(f"the length of matrix_y is:   {len(matrix_y)}")
        print(f"the length of matrix_x is:   {len(matrix_x)}")
        print(f"the length of matrix_y[0] is:   {len(matrix_y)}")

        return print(" The MATRIX_Y is not the rotation of MATRIX_X because the length of elements is different")

    num_rows_x, num_cols_x = len(matrix_x), len(matrix_x[0])
    for i in range(num_rows_x):
        for j in range(num_cols_x):
            if matrix_x[i][j] != matrix_y[j][i]:
                return print(" The MATRIX_Y is not the rotation of MATRIX_X ")

    return print(" The MATRIX_Y is the rotation of MATRIX_X ")


# rotation_matrix()

def invert_dictionary():
    value = int(input("Enter the number of Keys you want to enter in the dictionary:  "))
    user_dictionary = {}

    for i in range(value):
        key = input(f"Enter the {i + 1} key : ")
        value = input(f" Enter the {i + 1} value : ")

        user_dictionary[key] = value

    print(f" Before inverting: \n {user_dictionary}")

    invert_dictionary = {}

    for key, value in user_dictionary.items():
        if value in invert_dictionary:
            old_values = invert_dictionary[value]

            if type(old_values) is list:
                old_values.append(key)
            else:
                lst = [old_values, key]
                invert_dictionary[value] = lst

        else:
            invert_dictionary[value] = key

    print(f"After inverting:\n{invert_dictionary}")


# invert_dictionary()

def list_to_dictionary():
    number_of_inputs = int(input("Enter the number of user data you want to add to the system: "))
    all_user_data = {}

    for i in range(number_of_inputs):
        user_data = input("Enter the data of the user (First Name, Last Name, ID, Job Title, and Company): ").split()
        key = user_data[2]
        values = user_data[0:2] + user_data[3:5]
        all_user_data[key] = values

    print(f"All user data \n{all_user_data}")


# list_to_dictionary()

def is_palindrome(str, start_index, end_index):
    if start_index == end_index:
        return True

    if str[start_index] != str[end_index]:
        return False

    if start_index < end_index + 1:
        return is_palindrome(str, start_index + 1, end_index - 1)

def palindrome_check():
    s = input("Enter any word  :  ")
    palindrome = is_palindrome(s, 0, len(s)-1)

    if palindrome:
        print(f"{s} is a palindrome ")
    else:
        print(f"{s} is not a palindrome ")


palindrome_check()