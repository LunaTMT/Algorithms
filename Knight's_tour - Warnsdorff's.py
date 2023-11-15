"""Start at any initial position on the chessboard.

At each step, choose the next move by selecting the position with the fewest available moves.

Calculate the number of available moves from each potential next position.
Prioritize moves based on the number of subsequent available moves in ascending order.
Move the knight to the selected position.

Repeat steps 2-3 until the knight has visited every square on the chessboard.

Backtrack if a position is reached where no valid move is possible.
By consistently selecting moves that minimize the number of subsequent possibilities, 
Warnsdorff's algorithm increases the chances of finding a solution to the Knight's Tour problem. 
It's important to note that Warnsdorff's algorithm does not guarantee a solution for every chessboard, 
but it often provides reasonably quick solutions for many cases."""


def knights_tour(start, n):

    def is_valid_move(x, y, board):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def get_next_moves(x, y, board):
        return [(x + x2, y + y2) for (x2, y2) in zip(dx, dy) if is_valid_move(x + x2, y + y2, board)]

    def knights_tour_util(x, y, move_number, board, path):
        """
        knights_tour_util: This function is the core utility function responsible for recursively
        exploring and searching for a valid Knight's Tour on the chessboard. 
        The "util" part indicates its utility nature as it plays a crucial role in the overall algorithm.

        The use of "util" in function names is a common convention to signify that a function 
        is not meant to be used independently but rather serves as a utility or helper function for other parts
        of the program.

        So, knights_tour_util is a utility function designed to assist the main knights_tour function 
        in solving the Knight's Tour problem through recursive exploration and backtracking.
        """

        #Base Case - all recursion needs base case to break recursive loop
        if move_number == n**2: 
            path.append((x, y))
            return True

        #Generate Next Moves:
        moves = get_next_moves(x, y, board)

        """
        Given the current position and its possible new positions:
        - we sort these positions by how many moves they have
        moves[0] will be the position from x, y with the least possible moves (from move[0] x and y)
        """
        moves.sort(key=lambda pos: len(get_next_moves(*pos, board)))

        #Iterate Through Next Moves:
        for x_new, y_new in moves:
            #Make Move and Recursive Call:
            board[x_new][y_new] = move_number
            path.append((x_new, y_new))
            if knights_tour_util(x_new, y_new, move_number+1, board, path):
                return True

            #Backtracking:
            board[x_new][y_new] = -1
            path.pop()

        #No Solution is Found:
        return False

    start_x, start_y = start

    # Initialize the chessboard
    board = [[-1 for _ in range(n)] for _ in range(n)]
    path = [(start_x, start_y)]

    # Possible moves for a knight
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    # Set the starting position
    board[start_x][start_y] = 0

    # Find the knight's tour
    return path[:-1] if knights_tour_util(start_x, start_y, 1, board, path) else []