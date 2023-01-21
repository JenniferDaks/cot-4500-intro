import numpy as np


def create_3x3_matrix():
    # create the rows of the 3x3 matrix. start all values at 0
    row1 = np.zeros(3)
    row2 = np.zeros(3)
    row3 = np.zeros(3)
    #print(row1, row2, row3)

    # combine rows into an array to make the matrix
    matrix = np.array([row1, row2, row3])
    #print(matrix)

    return matrix


def problem1(matrix):
    # if i == j (if the row number and column number are equal) change the value from 0 to 1
    # start i and j at 0
    i: int = 0
    j: int = 0

    # iterate through rows
    for row in matrix:
        # iterate through columns
        for column in row:
            # if i == j, change value to 1. first iteration is i == j == 0
            if i == j:
                # change the value
                matrix[i][j] = 1
            # increment the value of j to check the next column in the same row
            j += 1
        # after iterating through all columns for a row, increment the value of i to check next row
        # and reset the counter for columns
        i += 1
        j = 0

    return matrix


def problem2(matrix):
    # if i ≠ j (if the row number and column number are not equal) add 3
    # start i and j at 0
    i: int = 0
    j: int = 0

    # iterate through rows
    for row in matrix:
        # iterate through columns
        for column in row:
            # if i ≠ j, add 3
            if i != j:
                # change the value
                matrix[i][j] += 3
            # increment the value of j to check the next column in the same row
            j += 1
        # after iterating through all columns for a row, increment value of i to check next row
        # and reset the counter for columns
        i += 1
        j = 0

    return matrix


def problem3(matrix):
    # delete the last column of each row
    new_matrix = [row[:-1] for row in matrix]

    return new_matrix


def print_matrix(matrix):
    # start i and j at 0
    i: int = 0
    j: int = 0

    # iterate through rows
    for row in matrix:
        # iterate through columns
        for column in row:
            # print
            print(int(matrix[i][j]), end=' ')
            # increment the value of j to the next column in the same row
            j += 1
        # after iterating through all columns for a row,
        # print a new line
        print("")
        # increment value of i to check next row
        # and reset the counter for columns
        i += 1
        j = 0

    print("")


if __name__ == "__main__":
    # Print a specific 3x3 matrix where a cell is 1 if i == j, else 0
    matrix1 = create_3x3_matrix()
    matrix1 = problem1(matrix1)
    # after changing all values of matrix1[i][j] from 0 to 1 where i == j , print it
    print_matrix(matrix1)

    # Print the 3x3 matrix from #1 and then add 3 to every cell where i ≠ j
    # start matrix2 with value of matrix1
    matrix2 = matrix1
    matrix2 = problem2(matrix2)
    # print matrix
    print_matrix(matrix2)

    # Print the 3x3 matrix from #2 as a 3x2 by deleting the last column from the matrix created
    # start matrix3 with value of matrix2
    matrix3 = matrix2
    matrix3 = problem3(matrix3)
    # print matrix
    print_matrix(matrix3)