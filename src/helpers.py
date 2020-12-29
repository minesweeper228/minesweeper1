import tkinter as tk


def center(win):
    win.update_idletasks()
    x = (win.winfo_screenwidth() // 2) - win.winfo_width()
    y = (win.winfo_screenheight() // 2) - win.winfo_height()
    win.geometry('{}x{}+{}+{}'.format(win.winfo_width(), win.winfo_height(), x, y))


def update_window_size(window, width, height):
    window.resizable(width=tk.FALSE, height=tk.FALSE)
    window.geometry('{}x{}'.format(width, height))


class Windows_Win():
    def __init__(self, master, size, mines, endgame):
        self.top = tk.Toplevel(master)
        self.top.resizable(width=tk.FALSE, height=tk.FALSE)
        self.top.geometry('{}x{}'.format(400, 250))
        self.top.configure(bg="light gray")
        center(self.top)

        text1 = tk.Label(self.top, text="Перемога!")
        text1.config(font=("Times New Roman", 14), fg="green", bg="light gray")
        text1.pack(pady=10)

        button6 = tk.Button( self.top, text="Вихід", bg="light green", height=2, width=15, command=endgame)
        button6.pack(side=tk.BOTTOM)


class Windows_Lose():
    def __init__(self, master, size, mines, endgame):
        self.top = tk.Toplevel(master)
        self.top.resizable(width=tk.FALSE, height=tk.FALSE)
        self.top.geometry('{}x{}'.format(400, 250))
        self.top.configure(background="light grey")
        center(self.top)

        text1 = tk.Label(self.top, text="Поразка!")
        text1.config(font=("Times New Roman", 14), fg="red", bg="light gray")
        text1.pack(pady=10)

        button8 = tk.Button(self.top, text="Вихід", bg="light green",height=2, width=15, command=endgame)
        button8.pack(side=tk.BOTTOM)
