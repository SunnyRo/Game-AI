def printBoard(board):
    """
    @brief: print out the sudoku board 9x9
    @param board: the board that is wanted to print out 
    @return: void
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("--- --- ---")
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end="")


def findZero(board):
    """
    @brief: find a zero from the board
    @param board: the sudoku board
    @return: row and column of a zero, or None if find nothing
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None


def checkValid(board, number, position):
    """
    @brief: check if the input number is valid
    @param board: the sudoku board
    @param number: the input number that wants to check
    @param position: the position that want to try the input number
    @return: True if the number is valid, False if its not
    """
    # check row
    for i in range(len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # check column
    for j in range(len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False
    # check the sub-gird
    boxRow = position[1] // 3  # foor division to it will be 0, 1 ,2 for i = 0 ->8
    boxColumn = position[0] // 3
    # check all element in the sub gird
    for i in range(boxColumn * 3, boxColumn * 3 + 3):
        for j in range(boxRow * 3, boxRow * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False
    # the number is valid return True
    return True


def sudokuSolver(board):
    """
    @brief: solve the sudoku
    @param board: the sudoku board
    @return: the solved sudoku board
    """
    zero = findZero(board)
    # zero = none return true else get row and column of that zero
    if not zero:
        return True
    else:
        row, column = zero
    # check if any number from 1 to 9 is valid for the current zero position
    for i in range(1, 10):
        if checkValid(board, i, (row, column)):  # if the current number is valid
            board[row][column] = i  # insert the value into the matrix
            # recursive call the sudoku solver again
            if sudokuSolver(board):
                return True
            # if false set the current element is zero
            board[row][column] = 0
    return False


# main
# open input1.txt then store the matrix into the board
with open("input1.txt", "r") as file:
    board = [[int(num) for num in line.split(" ")] for line in file]

sudokuSolver(board)
print("Solved Sudoku")
printBoard(board)
