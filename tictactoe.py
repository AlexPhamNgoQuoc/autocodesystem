# start the code

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the game board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if there's a winner
def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    # No winner
    return None

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        position = int(input("Enter a position (1-9): ")) - 1

        # Check if the position is valid
        if position < 0 or position >= 9 or board[position] != ' ':
            print("Invalid move. Try again.")
            continue

        # Update the board
        board[position] = current_player

        # Check if there's a winner
        winner = check_winner()
        if winner:
            print_board()
        # Check if there's a tie
        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

        print()

# Start the game
play_game()
# end the code
