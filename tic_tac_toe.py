def tic_tac_toe():
    def print_board(board):
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--|---|--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--|---|--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def get_move(player, board):
        while True:
            try:
                move = int(input(f"{player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    raise ValueError
                return move
            except ValueError:
                print("Invalid move. Try again.")

    def check_win(board):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))
        for w in wins:
            if board[w[0]] == board[w[1]] == board[w[2]] != " ":
                return board[w[0]]
        return None

    def play():
        board = [" "] * 9
        players = ("X", "O")
        current_player = 0
        winner = None

        while not winner and " " in board:
            print_board(board)
            move = get_move(players[current_player], board)
            board[move] = players[current_player]
            winner = check_win(board)
            current_player = (current_player + 1) % 2

        print_board(board)
        if winner:
            print(f"{winner} wins!")
        else:
            print("Tie game.")

    play()
tic_tac_toe()