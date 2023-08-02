from pprint import pprint
import os

board = [[2, 0, 2, 0],
         [2, 0, 2, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 2]]

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
            if c == columns - 1: 
                return False
        case "U":
            if r == 0: 
                return False
        case "D":
            if r == rows - 1:
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



direction = "L"
rows = columns = 4

while True:
    os.system("cls")
    print_board()
    direction = input("\n Dir : ")
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            
            if board[r][c] != 0:

                valid = find_next_free(direction, r, c)

                if valid:  
                    r_new, c_new = valid
                    
                    if board[r][c] == board[r_new][c_new]:
                        board[r_new][c_new] *= 2
                        board[r][c] = 0
                    else:
                        board[r][c], board[r_new][c_new] = board[r_new][c_new], board[r][c]

    
                        

