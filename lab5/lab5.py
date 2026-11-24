matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
players = ["X", "O"]
turns = 0
winner = None

def display_board():
    print()
    print("TIC-TAC-TOE")
    print()

    for row in matrix:
        print(" | ".join(row))

    print()

while turns < 9 and winner is None:

    display_board()

    player = players[turns % 2]

    print(player + "'s Turn")

    try:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        if row < 1 or row > 3 or col < 1 or col > 3:
            print()
            print("Invalid row or column. Please enter a number from 1-3.")
            input("Hit [enter] to continue.")
            continue

        row_index = row - 1
        col_index = col - 1

        if matrix[row_index][col_index] != "-":
            print()
            print(f"Someone has already claimed {row}:{col}!")
            print()
            input("Hit [enter] to continue.")
            continue

        matrix[row_index][col_index] = player

        for r in range(3):
            if (matrix[r][0] == player and
                matrix[r][1] == player and
                matrix[r][2] == player):
                winner = player

        for c in range(3):
            if (matrix[0][c] == player and
                matrix[1][c] == player and
                matrix[2][c] == player):
                winner = player

        if (matrix[0][0] == player and
            matrix[1][1] == player and
            matrix[2][2] == player):
            winner = player

        if (matrix[0][2] == player and
            matrix[1][1] == player and
            matrix[2][0] == player):
            winner = player

        turns += 1

    except ValueError:
        print()
        print("Invalid input. Please enter numbers only.")
        input("Hit [enter] to continue.")


display_board()

if winner is not None:
    print(winner + " won!")
else:
    print("It's a draw!")

print()
print("Game Over!")
print("Thanks for playing!")