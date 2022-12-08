def find_next_empty(puzzle):
    # finds next row, col on the puzzle that's not filled yet --> rep with -1
    # return (row,col) or (none, none) if there is none
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col
    
    return None, None

def is_valid(puzzle, guess, row, col):
    # figures out wether the guess at the row/col is a valid guess
    # start with row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if guess == puzzle[row][col]:
                return False
    
    return True

def solve_sudoku(puzzle):
    # step 1: choose open space
    row, col = find_next_empty(puzzle)

    # step 1.1: if prev function returns None -> board is filled and we are done
    if row is None:
        return True

    # step 2: make a guess on prev searched empty place
    for guess in range(1, 10):
        # step 3: check if this guess is valid
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

        # reset the guess if not valid or does not solve the puzzle
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    test_board = [
        [-1, -1, -1, 6, 8, -1, 9, -1, 5],
        [-1, -1, 4, -1, -1, 1, 8, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 6, -1],
        [-1, 3, -1, -1, 5, -1, -1, -1, 8],
        [-1, 4, -1, 2, -1, 3, -1, 5, -1],
        [2, -1, -1, -1, 9, -1, -1, 1, -1],
        [-1, 7, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 9, 1, -1, -1, 7, -1, -1],
        [1, -1, 8, -1, 4, 2, -1, -1, -1],
    ]
    print(solve_sudoku(test_board))
    print(test_board)