from PIL import ImageTk, Image
import tkinter as tk
import random
from helpers import Windows_Lose, Windows_Win
import os
from functools import partial


diffs = {
    'новачок': ((9, 9), 10),
    'любитель': ((16, 16), 40),
    'професіонал': ((16, 30), 90)
}


class Game:
    def __init__(self, root, diff_str, endgame):
        self.endgame = endgame
        self.diff_str = diff_str
        self.board_size, self.mines = diffs[diff_str]

        self.master = tk.Frame(root)
        self.master.pack()

        self.board_f = tk.Frame(self.master)

        self.flagged = 0
        self.total_flagged = 0

        self.image_size = 25
        self.img_bomb = ImageTk.PhotoImage(Image.open(
            "icons/bomb.png").resize((self.image_size, self.image_size)))
        self.img_flag = ImageTk.PhotoImage(Image.open(
            "icons/flag.png").resize((self.image_size, self.image_size)))
        self.img_empty = ImageTk.PhotoImage(Image.open(
            "icons/empty.png").resize((self.image_size, self.image_size)))
        self.img_default = ImageTk.PhotoImage(
            Image.open("icons/default.png").resize((self.image_size, self.image_size)))
        self.img_question = ImageTk.PhotoImage(
            Image.open("icons/question.png").resize((self.image_size, self.image_size)))
        self.img_1 = ImageTk.PhotoImage(Image.open(
            "icons/1.png").resize((self.image_size, self.image_size)))
        self.img_2 = ImageTk.PhotoImage(Image.open(
            "icons/2.png").resize((self.image_size, self.image_size)))
        self.img_3 = ImageTk.PhotoImage(Image.open(
            "icons/3.png").resize((self.image_size, self.image_size)))
        self.img_4 = ImageTk.PhotoImage(Image.open(
            "icons/4.png").resize((self.image_size, self.image_size)))
        self.img_5 = ImageTk.PhotoImage(Image.open(
            "icons/5.png").resize((self.image_size, self.image_size)))
        self.img_6 = ImageTk.PhotoImage(Image.open(
            "icons/6.png").resize((self.image_size, self.image_size)))
        self.img_7 = ImageTk.PhotoImage(Image.open(
            "icons/7.png").resize((self.image_size, self.image_size)))
        self.img_8 = ImageTk.PhotoImage(Image.open(
            "icons/8.png").resize((self.image_size, self.image_size)))
        self.images = {
            0: self.img_empty,
            1: self.img_1,
            2: self.img_2,
            3: self.img_3,
            4: self.img_4,
            5: self.img_5,
            6: self.img_6,
            7: self.img_7,
            8: self.img_8,
        }

        self.board = [[0 for k in range(self.board_size[1])]
                      for k in range(self.board_size[0])]
        self.status = [[0 for k in range(self.board_size[1])]
                       for k in range(self.board_size[0])]

        self.generate_mines()
        self.FindNeighors()
        self.game_part()

    def generate_mines(self):
        indexes = [(i, j) for j in range(self.board_size[1])
                   for i in range(self.board_size[0])]
        mines_location = random.sample(indexes, self.mines)
        for loc in mines_location:
            self.board[loc[0]][loc[1]] = -1

    def FindNeighors(self):
        for row in range(self.board_size[0]):
            for col in range(self.board_size[1]):
                n = 0
                if self.board[row][col] == -1:
                    continue
                if row-1 >= 0 and col-1 >= 0 and self.board[row-1][col-1] == -1:
                    n += 1
                if row-1 >= 0 and col >= 0 and self.board[row-1][col] == -1:
                    n += 1
                if row-1 >= 0 and col+1 < self.board_size[1] and self.board[row-1][col+1] == -1:
                    n += 1
                if row >= 0 and col-1 >= 0 and self.board[row][col-1] == -1:
                    n += 1
                if row >= 0 and col+1 < self.board_size[1] and self.board[row][col+1] == -1:
                    n += 1
                if row+1 < self.board_size[0] and col-1 >= 0 and self.board[row+1][col-1] == -1:
                    n += 1
                if row+1 < self.board_size[0] and col >= 0 and self.board[row+1][col] == -1:
                    n += 1
                if row+1 < self.board_size[0] and col+1 < self.board_size[1] and self.board[row+1][col+1] == -1:
                    n += 1
                self.board[row][col] = n

    def empty_cell(self, row, col):
        def work(row, col):
            number = self.board[row][col]
            self.buttons[row][col].configure(image=self.images[number])
            if self.status[row][col] == 2:
                self.total_flagged -= 1
            self.status[row][col] = 1
            if number == 0:
                self.empty_cell(row, col)

        if row-1 >= 0 and col-1 >= 0 and self.status[row-1][col-1] != 1:
            work(row-1, col-1)
        if row-1 >= 0 and col >= 0 and self.status[row-1][col] != 1:
            work(row-1, col)
        if row-1 >= 0 and col+1 < self.board_size[1] and self.status[row-1][col+1] != 1:
            work(row-1, col+1)
        if row >= 0 and col-1 >= 0 and self.status[row][col-1] != 1:
            work(row, col-1)
        if row >= 0 and col+1 < self.board_size[1] and self.status[row][col+1] != 1:
            work(row, col+1)
        if row+1 < self.board_size[0] and col-1 >= 0 and self.status[row+1][col-1] != 1:
            work(row+1, col-1)
        if row+1 < self.board_size[0] and col >= 0 and self.status[row+1][col] != 1:
            work(row+1, col)
        if row+1 < self.board_size[0] and col+1 < self.board_size[1] and self.status[row+1][col+1] != 1:
            work(row+1, col+1)

    def flag(self, coord, event=None):
        if self.status[coord[0]][coord[1]] == 0:
            self.buttons[coord[0]][coord[1]].configure(image=self.img_flag)

            if self.board[coord[0]][coord[1]] == -1:
                self.flagged += 1

            self.status[coord[0]][coord[1]] = 2
            self.total_flagged += 1
        elif self.status[coord[0]][coord[1]] == 2:
            self.buttons[coord[0]][coord[1]].configure(image=self.img_question)

            self.status[coord[0]][coord[1]] = 2
            self.total_flagged -= 1
        elif self.status[coord[0]][coord[1]] == 3:
            self.buttons[coord[0]][coord[1]].configure(image=self.img_default)

            self.status[coord[0]][coord[1]] = 0
            self.total_flagged -= 1
        self.labelText.set("Залишилось мін: " +
                           str(self.mines - self.total_flagged))

    def cell(self, coord, event=None):
        if self.board[coord[0]][coord[1]] == -1:
            self.buttons[coord[0]][coord[1]].configure(image=self.img_bomb)
            self.master.update_idletasks()
            self.Lose()

        if self.status[coord[0]][coord[1]] == 0:
            key = self.board[coord[0]][coord[1]]

            if key == 0:
                self.buttons[coord[0]][coord[1]].configure(
                    image=self.images[0])
                self.empty_cell(coord[0], coord[1])
            elif key > 0 and key <= 8:
                self.buttons[coord[0]][coord[1]].configure(
                    image=self.images[key])

            self.status[coord[0]][coord[1]] = 1
        elif self.status[coord[0]][coord[1]] == 2:
            self.buttons[coord[0]][coord[1]].configure(image=self.img_default)

            self.status[coord[0]][coord[1]] = 0
            self.total_flagged -= 1

        self.labelText.set("Залишилось мін:" +
                           str(self.mines - self.total_flagged))

        if (self.board_size[0] * self.board_size[1] - self.mines) == sum(x.count(1) for x in self.status):
            self.Win()

    def game_part(self):
        self.buttons = [[0 for k in range(self.board_size[1])]
                        for k in range(self.board_size[0])]

        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                self.buttons[i][j] = tk.Label(self.board_f)
                self.buttons[i][j].configure(image=self.img_default)
                self.buttons[i][j].grid(row=i, column=j)

                self.buttons[i][j].bind(
                    "<Button-1>", partial(self.cell, (i, j)))
                self.buttons[i][j].bind(
                    "<Button-3>", partial(self.flag, (i, j)))

        self.labelText = tk.StringVar()
        self.labelText.set("Залишилось мін: " + str(self.mines))
        text2 = tk.Label(self.master, textvariable=self.labelText)
        text2.config(font=("Times New Roman", 14))
        text2.pack(side=tk.BOTTOM)
        self.board_f.pack()

    def Win(self):
        Windows_Win(self.master, self.board_size, self.mines,
                    lambda: self.endgame(self.diff_str, True))

    def Lose(self):
        Windows_Lose(self.master, self.board_size, self.mines,
                     lambda: self.endgame(self.diff_str, False))
