import tkinter as tk
from helpers import center
from tkinter import ttk


class ResultsTable:
    def __init__(self, root, auth):
        self.USI = 'Усі'

        self.top = tk.Toplevel(root)
        self.top.resizable(width=tk.FALSE, height=tk.FALSE)
        self.top.geometry('{}x{}'.format(400, 250))
        self.top.configure(bg="light gray")
        center(self.top)

        self.results = auth.get_all_results()
        self.results.sort(key=lambda a: a[1].date, reverse=True)
        self.player_logins = list(set(map(lambda a: a[0].login, self.results)))

        choices = [self.USI] + self.player_logins
        self.cmbb_user = ttk.Combobox(
            self.top, values=choices, state="readonly", width=15)
        self.cmbb_user.current(0)
        self.cmbb_user.bind("<<ComboboxSelected>>", self.show_users)
        self.cmbb_user.pack()

        self.lstb_results = tk.Listbox(self.top, height=20, width=50)
        self.show_users()
        self.lstb_results.pack(padx=4)

    def show_users(self, event=None):
        self.lstb_results.delete(0, tk.END)

        login = self.cmbb_user.get()
        if login == self.USI:
            results = self.results
        else:
            results = list(filter(lambda a: a[0].login == login, self.results))

        for result in results:
            player = result[0]
            res = result[1]
            win = 'перемога!' if res.is_win else 'поразка!'
            string = ' {}, {}, {}'.format(
                player.login, win, res.difficulty)
            self.lstb_results.insert(tk.END, string)
