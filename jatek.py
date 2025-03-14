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

def player_move(board, row, col, buttons):
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
            buttons[0][0].after(1000, lambda: computer_move(board, buttons))

def computer_move(board, buttons):
    empty_cells = get_empty_cells(board)
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"
    buttons[move[0]][move[1]].config(text="O", state="disabled")
    if check_winner(board, "O"):
        messagebox.showinfo("Játék vége", "A gép nyert!")
        reset_game(board, buttons)
    elif not get_empty_cells(board):
        messagebox.showinfo("Játék vége", "Döntetlen!")
        reset_game(board, buttons)

def reset_game(board, buttons):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text="", state="normal")

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    root = tk.Tk()
    root.title("Tic-tac-toe")
    
    buttons = [[None for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text="", width=10, height=3, 
                               command=lambda i=i, j=j: player_move(board, i, j, buttons))
            button.grid(row=i, column=j)
            buttons[i][j] = button
    
    root.mainloop()

if __name__ == "__main__":
    main()