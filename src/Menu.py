import tkinter as tk
from helpers import center
from Game import Game


class Menu():
    def __init__(self, root, start_game, results, conf_game):
        self.root = root
        self.root.pack(fill=tk.BOTH, expand=True)
        self.root.configure(bg="light blue")

        self.master = tk.Frame(root)
        self.master.pack(expand=True)
        self.master.configure(bg="light blue")

        button1 = tk.Button(self.master, text="Новачок(9 x 9)", height=3, width=20, bg="light yellow", font=(
            "Times New Roman", 14), command=lambda: start_game('новачок'))
        button1.pack(pady=5)

        button2 = tk.Button(self.master, text="Любитель(16 x 16)", height=3, width=20, bg="light yellow", font=(
            "Times New Roman", 14), command=lambda: start_game('любитель'))
        button2.pack(pady=5)

        button3 = tk.Button(self.master, text="Професіонал(16 x 30)", height=3, width=20, bg="light yellow", font=(
            "Times New Roman", 14), command=lambda: start_game('професіонал'))
        button3.pack(pady=5)

        button3 = tk.Button(self.master, text="Таблиця результатів", height=3, width=20, bg="light yellow", font=(
            "Times New Roman", 14), command=results)
        button3.pack(pady=5)

        button4 = tk.Button(self.master, text="Вихід", height=3, width=20, bg="light yellow", font=(
            "Times New Roman", 14), command=conf_game)
        button4.pack(pady=5)
