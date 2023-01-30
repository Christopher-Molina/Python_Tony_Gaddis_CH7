# Starting Out With Pyth 5th Edition: Chapter 7 - Exercise 11
MAGIC_CONSTANT = 15


def main():
    try:
        # Input 3 row 3 column matrix to evaluate
        matrix = get_matrix()

        # Calculate each row sum
        row_sums = get_row_sums(matrix)

        # Calculate each column sum
        col_sums = get_col_sums(matrix)

        # Calculate each diagonal sum
        left_diagonal = get_left_sum(matrix)
        right_diagonal = get_right_sum(matrix)

        # Evaluate matrix
        evaluate(matrix, row_sums, col_sums, left_diagonal, right_diagonal)
    except (IndexError, TypeError, ValueError, ZeroDivisionError) as e:
        print(e)


# Function returns a matrix
def get_matrix():
    # Input rows
    rows = int(input('Number of Rows: '))

    # Input columns
    cols = int(input('Number of Columns: '))

    # Initialize matrix
    matrix = []
    for row in range(0, cols):
        matrix.append([])

    for row in range(0, rows):
        for col in range(0, cols):
            matrix[row].append(col)
            matrix[row][col] = 0

    for row in range(0, rows):
        print(f'\nEntry in Row {row + 1}:')
        for col in range(0, cols):
            print(f'Column {col+1}: ', end=' ')
            matrix[row][col] = int(input())

    # Return the matrix
    return matrix


# Function evaluates whether each row sums to magic constant
def get_row_sums(matrix):
    # Evaluate each row sum
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[row][col]
    return total / len(matrix)


# Function evaluates whether each column sums to magic constant
def get_col_sums(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[col][row]
    return total / len(matrix)


# Function gets sum of left diagonal
def get_left_sum(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row == col:
                total += matrix[row][col]
    return total


# Function gets sum of right diagonal
def get_right_sum(matrix):
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (row + col) == len(matrix) - 1:
                total += matrix[row][col]
    return total


# Function evaluates whether the given matrix is a lo shu magic square
def evaluate(matrix, row_sums, col_sums, left_sum, right_sum):
    # Display matrix
    print('\nMatrix:')
    for line in matrix:
        print(' '.join(map(str, line)))

    if (row_sums == MAGIC_CONSTANT) and (col_sums == MAGIC_CONSTANT)\
            and (left_sum == MAGIC_CONSTANT) and (right_sum == MAGIC_CONSTANT):
        print('\nMatrix is a Lo Shu Magic Square.')
    else:
        print('\nMatrix is Not a Lo Shu Magic Square.')


# Call the main function
if __name__ == '__main__':
    main()
