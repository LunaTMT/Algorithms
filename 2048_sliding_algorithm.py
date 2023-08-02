from pprint import pprint
from random import choices
from random import randint
import os

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

opposite = { "L" : "R",
             "R" : "L",
             "U" : "D",
             "D" : "U"}


def print_board():
    for r in board:
        print(r)


#2048 sliding algorithm

def get_next_directional_position(dir, r, c):
    match dir:
        case "L":
            return (r, c-1)
        case "R":
            return (r, c+1)
        case "U":
            return (r-1, c)
        case "D":
            return (r+1, c)

def find_next_free(direction, r, c):
    
    """
    If the position passed is an edge case we cannot go any further
    for example, if the direction is left and our position is (x,0) 
    x, 0, 0, 0 
    x, 0, 0, 0
    x, 0, 0, 0
    x, 0, 0, 0
    Then we cannot find get a new position as it is already in the most left position
    The same also holds for Right, Up, and Down
    """
    match direction:
        case "L":
            if c == 0: 
                return False
        case "R":
            if c == columns: 
                return False
        case "U":
            if r == 0: 
                return False
        case "D":
            if r == rows:
                return False
    """
    Given the position is not an "edge" wecan proceedto find the new position"""
    r_new, c_new = get_next_directional_position(direction, r, c)

    if direction in ("L", "R"):
        while (0 < c_new < columns) and board[r_new][c_new] == 0:
            r_new, c_new = get_next_directional_position(direction, r_new, c_new)
    
    if direction in ("U", "D"):
        while (0 < r_new < rows) and board[r_new][c_new] == 0:
            r_new, c_new = get_next_directional_position(direction, r_new, c_new)


    return r_new, c_new

def shift(direction, r, c):

    if board[r][c] != 0:

        valid = find_next_free(direction, r, c)

        if valid:  
            r_new, c_new = valid
            
            if board[r][c] == board[r_new][c_new]:
                board[r_new][c_new] *= 2
                board[r][c] = 0
            elif board[r_new][c_new] == 0:
                board[r][c], board[r_new][c_new] = board[r_new][c_new],  board[r][c]
            else:
                r_new, c_new = get_next_directional_position(opposite[direction], r_new, c_new) #we get the position just before (which is the opposite)
                board[r][c], board[r_new][c_new] = board[r_new][c_new],  board[r][c]
                
def spawn_random():
    #10% chance for 4 spawning
    #90% chance for 2 spawning
    block = choices(population=[2, 4], weights=[0.90, 0.10])[0]
    r, c = randint(0, rows), randint(0, columns)
    while board[r][c] != 0:
        r, c = randint(0, rows), randint(0, columns)
    board[r][c] = block
    
    

direction = "L"
rows = columns = 3

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

    if direction in ("L", "U"):
        for r, row in enumerate(board):
            for c, item in enumerate(row):
                shift(direction, r, c)
    
    if direction in ("R", "D"):
        for r, row in enumerate(board):
            for c in range(columns-1, -1, -1):
                shift(direction, r, c)
           
                
    


                        

