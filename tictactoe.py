import random

def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

def check_winner(board, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],   
        [0,3,6], [1,4,7], [2,5,8],   
        [0,4,8], [2,4,6]             
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw(board):
    return " " not in board

def empty_cells(board):
    return [i for i in range(9) if board[i] == " "]


def ai_move(board, ai_player, human_player):
    # 1. Try to win
    for cell in empty_cells(board):
        board[cell] = ai_player
        if check_winner(board, ai_player):
            board[cell] = " "
            return cell
        board[cell] = " "

    # 2. Block human from winning
    for cell in empty_cells(board):
        board[cell] = human_player
        if check_winner(board, human_player):
            board[cell] = " "
            return cell
        board[cell] = " "

    # 3. Take center if free
    if board[4] == " ":
        return 4

    # 4. Take a corner if free
    corners = [0, 2, 6, 8]
    free_corners = [c for c in corners if board[c] == " "]
    if free_corners:
        return random.choice(free_corners)

    # 5. Otherwise take any free edge
    return random.choice(empty_cells(board))

def play_game():
    board = [" "] * 9
    human = "X"
    ai = "O"
    current_player = "X"  # human starts first

    print("Welcome to Tic-Tac-Toe: Human vs AI!")
    print("You are X, AI is O.")
    print("Positions are numbered 0-8 as shown:")
    print_board([str(i) for i in range(9)])

    while True:
        print_board(board)

        if current_player == human:
            try:
                move = int(input("Your turn (0-8): "))
            except ValueError:
                print("Invalid input. Enter a number between 0 and 8.")
                continue

            if move < 0 or move > 8:
                print("Position out of range. Try again.")
                continue
            if board[move] != " ":
                print("Cell already taken. Choose another.")
                continue

            board[move] = human

        else:
            print("AI's turn...")
            move = ai_move(board, ai, human)
            board[move] = ai
            print(f"AI chose position {move}")

        if check_winner(board, current_player):
            print_board(board)
            winner_name = "You" if current_player == human else "AI"
            print(f"{winner_name} win{'s' if winner_name == 'AI' else ''}!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = ai if current_player == human else human

if __name__ == "__main__":
    play_game()