import tkinter as tk
from game_env.game import GoGame

class GoGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Go Game")
        self.canvas_size = 600
        self.cell_size = self.canvas_size // self.game.board_size
        self.canvas = tk.Canvas(self.root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_event)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        # Draw grid lines
        for i in range(self.game.board_size):
            # Vertical lines
            x = i * self.cell_size + self.cell_size // 2
            self.canvas.create_line(
                x, self.cell_size // 2, x, self.canvas_size - self.cell_size // 2
            )
            # Horizontal lines
            y = i * self.cell_size + self.cell_size // 2
            self.canvas.create_line(
                self.cell_size // 2, y, self.canvas_size - self.cell_size // 2, y
            )
        # Draw stones
        for y in range(self.game.board_size):
            for x in range(self.game.board_size):
                stone = self.game.board[y][x]
                if stone != 0:
                    self.draw_stone(x, y, stone)

    def draw_stone(self, x, y, player):
        xc = x * self.cell_size + self.cell_size // 2
        yc = y * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 2 - 2
        color = "black" if player == 1 else "white"
        self.canvas.create_oval(
            xc - radius, yc - radius, xc + radius, yc + radius, fill=color
        )

    def click_event(self, event):
        x = event.x // self.cell_size
        y = event.y // self.cell_size
        if self.game.make_move(x, y):
            self.draw_board()
            if self.game.is_game_over():
                winner = self.game.get_winner()
                msg = "Game Over. Winner: " + ("Black" if winner == 1 else "White")
                tk.messagebox.showinfo("Game Over", msg)

    def start(self):
        self.root.mainloop()