# TicTacToe game with child-friendly graphics and three difficulty levels

import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe for Kids")
        self.root.configure(bg="skyblue")
        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        self.buttons = []
        self.board = ['' for _ in range(9)]
        self.difficulty = None
        self.create_start_screen()

    def create_start_screen(self):
        # Difficulty selection window
        self.start_frame = tk.Frame(self.root, bg="skyblue")
        self.start_frame.pack(expand=True, fill="both")
        title = tk.Label(self.start_frame, text="Willkommen zum Tic Tac Toe!", font=("Comic Sans MS", 24, "bold"), bg="skyblue")
        title.pack(pady=20)
        info = tk.Label(self.start_frame, text="Bitte w\u00e4hle den Schwierigkeitsgrad", font=("Comic Sans MS", 16), bg="skyblue")
        info.pack(pady=10)

        btn_easy = tk.Button(self.start_frame, text="Leicht", font=("Comic Sans MS", 14), command=lambda: self.start_game('easy'), width=10, bg="lightgreen")
        btn_easy.pack(pady=5)
        btn_medium = tk.Button(self.start_frame, text="Mittel", font=("Comic Sans MS", 14), command=lambda: self.start_game('medium'), width=10, bg="orange")
        btn_medium.pack(pady=5)
        btn_hard = tk.Button(self.start_frame, text="Schwer", font=("Comic Sans MS", 14), command=lambda: self.start_game('hard'), width=10, bg="red")
        btn_hard.pack(pady=5)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.start_frame.destroy()
        self.build_board()

    def build_board(self):
        board_frame = tk.Frame(self.root, bg="skyblue")
        board_frame.pack(expand=True)
        for i in range(9):
            btn = tk.Button(board_frame, text="", font=("Comic Sans MS", 36, "bold"), width=3, height=1,
                             command=lambda idx=i: self.player_move(idx), bg="lightyellow")
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

    def player_move(self, index):
        if self.board[index] == '' and not self.check_winner(self.board):
            self.board[index] = self.player_symbol
            self.buttons[index].configure(text=self.player_symbol, disabledforeground="blue")
            self.buttons[index].config(state="disabled")
            if not self.check_game_end():
                self.root.after(500, self.computer_move)

    def computer_move(self):
        if self.difficulty == 'easy':
            move = self.random_move()
        elif self.difficulty == 'medium':
            move = self.medium_move()
        else:
            move = self.best_move()

        if move is not None:
            self.board[move] = self.computer_symbol
            self.buttons[move].configure(text=self.computer_symbol, disabledforeground="darkred")
            self.buttons[move].config(state="disabled")
        self.check_game_end()

    def random_move(self):
        available = [i for i, v in enumerate(self.board) if v == '']
        return random.choice(available) if available else None

    def medium_move(self):
        # Winning move
        for idx in range(9):
            if self.board[idx] == '':
                temp = self.board.copy()
                temp[idx] = self.computer_symbol
                if self.check_winner(temp) == self.computer_symbol:
                    return idx
        # Blocking move
        for idx in range(9):
            if self.board[idx] == '':
                temp = self.board.copy()
                temp[idx] = self.player_symbol
                if self.check_winner(temp) == self.player_symbol:
                    return idx
        return self.random_move()

    def best_move(self):
        best_score = -float('inf')
        move = None
        for idx in range(9):
            if self.board[idx] == '':
                self.board[idx] = self.computer_symbol
                score = self.minimax(self.board, False)
                self.board[idx] = ''
                if score > best_score:
                    best_score = score
                    move = idx
        return move

    def minimax(self, board_state, is_maximizing):
        winner = self.check_winner(board_state)
        if winner == self.computer_symbol:
            return 1
        elif winner == self.player_symbol:
            return -1
        elif '' not in board_state:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for idx in range(9):
                if board_state[idx] == '':
                    board_state[idx] = self.computer_symbol
                    score = self.minimax(board_state, False)
                    board_state[idx] = ''
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for idx in range(9):
                if board_state[idx] == '':
                    board_state[idx] = self.player_symbol
                    score = self.minimax(board_state, True)
                    board_state[idx] = ''
                    best_score = min(best_score, score)
            return best_score

    def check_winner(self, board_state):
        wins = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in wins:
            if board_state[a] and board_state[a] == board_state[b] == board_state[c]:
                return board_state[a]
        return None

    def check_game_end(self):
        winner = self.check_winner(self.board)
        if winner:
            messagebox.showinfo("Spiel beendet", f"{winner} hat gewonnen!")
            self.reset_game()
            return True
        elif '' not in self.board:
            messagebox.showinfo("Spiel beendet", "Unentschieden!")
            self.reset_game()
            return True
        return False

    def reset_game(self):
        for btn in self.buttons:
            btn.destroy()
        self.buttons = []
        self.board = ['' for _ in range(9)]
        self.create_start_screen()

if __name__ == '__main__':
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
