import random

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board, player):
    # Ellenőrzi a sorokat, oszlopokat és átlókat
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def player_move(board):
    while True:
        try:
            row = int(input("Add meg a sor számát (0, 1, 2): "))
            col = int(input("Add meg az oszlop számát (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Ez a hely már foglalt!")
        except (ValueError, IndexError):
            print("Érvénytelen lépés. Próbáld újra.")

def computer_move(board):
    empty_cells = get_empty_cells(board)
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Gratulálok, nyertél!")
            break
        if not get_empty_cells(board):
            print("Döntetlen!")
            break
        
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("A gép nyert!")
            break
        if not get_empty_cells(board):
            print("Döntetlen!")
            break

if __name__ == "__main__":
    main()