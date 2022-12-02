import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
    
    def get_num_neighboring_bombs(self, row, col):
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        
        return num_neighboring_bombs

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row-1), min(self.dim_size, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size, (col+1)+1)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)        
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# class Game():
#     def __init__(self, size=7, mine_amount=10):
#         self.size = size
#         self.board = [[]]
#         self.mine_amount = mine_amount
#         self.mine_list = set()

#     def create_board(self):
#         self.board = [[[' '] for rows in range(self.size)] for columns in range(self.size)]
#         return

#     def set_mines(self):
#         while self.mine_amount > len(self.mine_list):
#             self.mine_list.add((random.randint(0, self.size-1), random.randint(0, self.size-1)))
#         self.mine_list = list(self.mine_list)
    
#     def get_mine(self, x, y):
#         return (x, y) in self.mine_list
    
#     def draw_board(self):
#         print('|'.join(str(x) for x in range(self.size)))
#         for y, row in enumerate(self.board):
#             print(str(y) + ('|' + node + '|' for node in row[y]))

def play(dim_size=9, num_bombs=10):
    '''
        1. create board
        2. place mines
        3. take player input
        4. update board
        5. win condition
    '''
    # game = Game(dim_size, num_bombs)
    # game.create_board()
    # game.set_mines()
    # game.draw_board()

    board = Board(dim_size, num_bombs)

    safe = True

    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print('Invalid location.')
            continue

        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break

    if safe:
        print('won')
    else:
        print('lose')
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()