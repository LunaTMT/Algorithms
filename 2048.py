from pprint import pprint
from random import choices
from random import randint
import os

board = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [2, 2, 2, 8, 4, 4],]

opposite = { "L" : "R",
             "R" : "L",
             "U" : "D",
             "D" : "U"}


def print_board():
    for r in board:
        print(r)


#2048 sliding algorithm

def get_next_position(dir, position):
    r, c = position

    match dir:
        case "L":
            return (r, c-1)
        case "R":
            return (r, c+1)
        case "U":
            return (r-1, c)
        case "D":
            return (r+1, c)


def shift(direction, r, c, locked_positions):
    
    if board[r][c] != 0:
    
        new_position = r_new, c_new =  get_next_position(direction, (r, c))
        positions = [(r_new, c_new)]

        while (0 <= r_new < rows) and (0 <= c_new < columns):

            if board[r][c] == board[r_new][c_new]:
                if new_position in locked_positions: break

                locked_positions.add((new_position))
                board[r_new][c_new] *= 2 
                board[r][c] = 0
                return

            elif board[r_new][c_new] not in (0, board[r][c]):
                break

            new_position = r_new, c_new = get_next_position(direction, (r_new, c_new))
            positions.append((new_position))

        if len(positions) >= 2:
            r_new, c_new = positions[-2]
            board[r][c], board[r_new][c_new] = board[r_new][c_new], board[r][c]  

        print()   
            



                
def spawn_random():
    #10% chance for 4 spawning
    #90% chance for 2 spawning
    block = choices(population=[2, 4], weights=[0.90, 0.10])[0]
    r, c = randint(0, rows-1), randint(0, columns-1)
    while board[r][c] != 0:
        r, c = randint(0, rows-1), randint(0, columns-1)
    board[r][c] = block
    
    

direction = "L"
rows = len(board)
columns = len(board[0])

while True:
    clear = lambda: os.system('clear')
    clear()
    spawn_random()
    print_board()
    direction = input("\n Dir : ")

    """
    first-check
    left c = 0 -> columns
    right c = columns -> 0

    up r = 0 -> rows
    down r = rows -> 0
    """
    #print(rows, columns)0

    if direction in ("R", "D"):
        for row in reversed(range(rows)):
            locked_positions = set()
            for column in reversed(range(columns)):
                shift(direction, row, column, locked_positions)
    else:
        for row in range(rows):
            locked_positions = set()
            for column in range(columns):
                shift(direction, row, column, locked_positions)
        
   # input()


                        

