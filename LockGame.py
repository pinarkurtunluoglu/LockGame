import numpy as np

def create_board(size, player1_char, player2_char):
    board = np.full((size + 2, size + 2), ' ')
    board[0][1:-1] = [chr(ord('A') + i) for i in range(size)]
    board[size + 1][1:-1] = [chr(ord('A') + i) for i in range(size)]
    board[1:-1, 0] = [str(i) for i in range(1, size + 1)]
    board[1:-1, size + 1] = [str(i) for i in range(1, size + 1)]
    board[0][0] = ' '
    board[0][size + 1] = ' '
    board[size + 1][0] = ' '
    board[size + 1][size + 1] = ' '
    board[1][1:-1] = player2_char  # Player 2's pieces
    board[size][1:-1] = player1_char  # Player 1's pieces
    return board

def print_board(board):
    for row in board:
        print("+" + "---+" * len(row))
        print(f"| {' | '.join(row)} |")
    print("+" + "---+" * len(board[0]))

def check_valid_move(board, current_pos, target_pos, player):
    if current_pos[0] < 1 or current_pos[0] > len(board) - 2 or \
       current_pos[1] < 1 or current_pos[1] > len(board[0]) - 2 or \
       target_pos[0] < 1 or target_pos[0] > len(board) - 2 or \
       target_pos[1] < 1 or target_pos[1] > len(board[0]) - 2:
        return False  # Pieces cannot move outside the board

    current_piece = board[current_pos[0]][current_pos[1]]
    target_piece = board[target_pos[0]][target_pos[1]]
    
    # It should be the player's turn and the target position should be empty
    if current_piece == player and target_piece == ' ':
        # Check if the move is horizontal or vertical
        if current_pos[0] == target_pos[0]:  # Horizontal move
            start = min(current_pos[1], target_pos[1])
            end = max(current_pos[1], target_pos[1])
            for column in range(start + 1, end):
                if board[current_pos[0]][column] != ' ':
                    print("Warning: You cannot jump over another piece!")
                    return False
        elif current_pos[1] == target_pos[1]:  # Vertical move
            start = min(current_pos[0], target_pos[0])
            end = max(current_pos[0], target_pos[0])
            for row in range(start + 1, end):
                if board[row][current_pos[1]] != ' ':
                    print("Warning: You cannot jump over another piece!")
                    return False
        else:  # Diagonal move
            print("Warning: You can only make horizontal or vertical moves!")
            return False
        
        return True
    else:
        return False


def check_winner(board, player1_char, player2_char):
    player1_pieces = 0
    player2_pieces = 0
    for row in board:
        for piece in row:
            if piece == player1_char:
                player1_pieces += 1
            elif piece == player2_char:
                player2_pieces += 1
    
    if player1_pieces == 0:
        print(f"All pieces of {player1_char} player are locked. {player2_char} player wins!")
        return True  # End the game if all pieces of player 1 are out of the board
    elif player2_pieces == 0:
        print(f"All pieces of {player2_char} player are locked. {player1_char} player wins!")
        return True  # End the game if all pieces of player 2 are out of the board

    return False

def remove_piece(board, x, y):
    board[x][y] = ' '
    
def check_corner(board,target_pos):
    x, y = target_pos
    piece = board[x][y]
    
    if board[x][y - 1] != ' ' and board[x][y - 1] != piece:
        if (board[x - 1][y - 1] != ' ' and board[x - 1][y - 1] == piece) or (board[x + 1][y - 1] != ' ' and board[x + 1][y - 1] == piece):
            remove_piece(board, x, y-1)
            print(f"Piece at position {chr(ord('A') + y - 2)}{x} is locked and removed.")

    if board[x][y + 1] != ' ' and board[x][y + 1] != piece:
        if (board[x - 1][y + 1] != ' ' and board[x - 1][y + 1] == piece) or (board[x + 1][y + 1] != ' ' and board[x + 1][y + 1] == piece):
            remove_piece(board, x, y+1)
            print(f"Piece at position {chr(ord('A') + y)}{x} is locked and removed.")

    if board[x - 1][y] != ' ' and board[x - 1][y] != piece:
        if (board[x - 1][y - 1] != ' ' and board[x - 1][y - 1] == piece) or (board[x - 1][y + 1] != ' ' and board[x - 1][y + 1] == piece):
            remove_piece(board, x-1, y)
            print(f"Piece at position {chr(ord('A') + y - 1)}{x - 1} is locked and removed.")
            
    if board[x + 1][y] != ' ' and board[x + 1][y] != piece:
        if (board[x + 1][y - 1] != ' ' and board[x + 1][y - 1] == piece) or (board[x + 1][y + 1] != ' ' and board[x + 1][y + 1] == piece):
            remove_piece(board, x+1, y)
            print(f"Piece at position {chr(ord('A') + y - 1)}{x - 1} is locked and removed.")

            
            
def check_and_remove_piece(board, target_pos):
    x, y = target_pos
    piece = board[x][y]
    
    # Check left pieces
    if y - 2 >= 0 and board[x][y - 2] == piece:
        if board[x][y - 1] != ' ' and board[x][y - 1] != piece:
            remove_piece(board, x, y-1)  # Remove the piece
            print(f"Piece at position {chr(ord('A') + y - 2)}{x} is locked and removed.")

    # Check right pieces
    if y + 2 < len(board[0]) and board[x][y + 2] == piece:
        if board[x][y + 1] != ' ' and board[x][y + 1] != piece:
            remove_piece(board, x, y+1)  # Remove the piece
            print(f"Piece at position {chr(ord('A') + y)}{x} is locked and removed.")

    # Check top pieces
    if x - 2 >= 0 and board[x - 2][y] == piece:
        if board[x - 1][y] != ' ' and board[x - 1][y] != piece:
            remove_piece(board, x-1, y)  # Remove the piece
            print(f"Piece at position {chr(ord('A') + y - 1)}{x - 1} is locked and removed.")

    # Check bottom pieces
    if x + 2 < len(board) and board[x + 2][y] == piece:
        if board[x + 1][y] != ' ' and board[x + 1][y] != piece:
            remove_piece(board, x+1, y)  # Remove the piece
            print(f"Piece at position {chr(ord('A') + y - 1)}{x + 1} is locked and removed.")

def play_game():
    size = int(input("Enter the board size (4-8): "))
    player1_char = input("Enter the character for player 1: ")
    player2_char = input("Enter the character for player 2: ")
    board = create_board(size, player1_char, player2_char)

    print("Welcome to the game!")
    print_board(board)

    turn = 1
    while True:
        player = player1_char if turn % 2 != 0 else player2_char
        move = input(f"Make a move for {player} player (e.g., 8A 6D): ").replace(' ', '')
        if len(move) != 4:
            print("Invalid move format. Please enter the correct row number and column letter.")
            continue

        try:
            current_pos = (int(move[0]), ord(move[1].upper()) - ord('A') + 1)
            target_pos = (int(move[2]), ord(move[3].upper()) - ord('A') + 1)
        except (ValueError, IndexError):
            print("Invalid move format. Please enter the correct row number and column letter.")
            continue

        if check_valid_move(board, current_pos, target_pos, player):           
            board[target_pos[0]][target_pos[1]] = board[current_pos[0]][current_pos[1]]
            board[current_pos[0]][current_pos[1]] = ' '
            check_and_remove_piece(board, target_pos)
            check_corner(board,target_pos)
            print_board(board)

            if check_winner(board, player1_char, player2_char):
                break
            turn += 1
        else:
            print("Invalid move. Please try again.")

    print("Game over!")
    replay = input("Do you want to play again? (Y/N): ")
    if replay.upper() == "Y":
        play_game()
    else:
        print("Goodbye!")

play_game()
