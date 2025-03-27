import tkinter as tk
from tkinter import messagebox
import random

def check_winner(board, player):
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

def player_move(board, row, col, buttons, difficulty):
    if board[row][col] == " ":
        board[row][col] = "X"
        buttons[row][col].config(text="X", state="disabled")
        if check_winner(board, "X"):
            messagebox.showinfo("Játék vége", "Gratulálok, nyertél!")
            reset_game(board, buttons)
        elif not get_empty_cells(board):
            messagebox.showinfo("Játék vége", "Döntetlen!")
            reset_game(board, buttons)
        else:
            buttons[0][0].after(1000, lambda: computer_move(board, buttons, difficulty))

def computer_move(board, buttons, difficulty):
    if difficulty == "Könnyű":
        empty_cells = get_empty_cells(board)
        move = random.choice(empty_cells)
    elif difficulty == "Nehéz":
        _, move = minimax(board, True)
    
    board[move[0]][move[1]] = "O"
    buttons[move[0]][move[1]].config(text="O", state="disabled")
    if check_winner(board, "O"):
        messagebox.showinfo("Játék vége", "A gép nyert!")
        reset_game(board, buttons)
    elif not get_empty_cells(board):
        messagebox.showinfo("Játék vége", "Döntetlen!")
        reset_game(board, buttons)

def minimax(board, is_maximizing):
    winner = None
    if check_winner(board, "X"):
        return -1, None
    if check_winner(board, "O"):
        return 1, None
    if not get_empty_cells(board):
        return 0, None

    if is_maximizing:
        best_score = -float("inf")
        best_move = None
        for (i, j) in get_empty_cells(board):
            board[i][j] = "O"
            score, _ = minimax(board, False)
            board[i][j] = " "
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for (i, j) in get_empty_cells(board):
            board[i][j] = "X"
            score, _ = minimax(board, True)
            board[i][j] = " "
            if score < best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move

def reset_game(board, buttons):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text="", state="normal")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    root = tk.Tk()
    root.title("Tic-tac-toe")
    
    difficulty = tk.StringVar(value="Könnyű")
    
    difficulty_frame = tk.Frame(root)
    difficulty_frame.grid(row=0, column=0, columnspan=3)
    tk.Label(difficulty_frame, text="Nehézségi szint:").pack(side=tk.LEFT)
    tk.Radiobutton(difficulty_frame, text="Könnyű", variable=difficulty, value="Könnyű").pack(side=tk.LEFT)
    tk.Radiobutton(difficulty_frame, text="Nehéz", variable=difficulty, value="Nehéz").pack(side=tk.LEFT)
    
    buttons = [[None for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text="", width=10, height=3, 
                               command=lambda i=i, j=j: player_move(board, i, j, buttons, difficulty.get()))
            button.grid(row=i+1, column=j)  
            buttons[i][j] = button
    
    root.mainloop()

if __name__ == "__main__":
    main()