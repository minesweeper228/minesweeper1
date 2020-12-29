import tkinter as tk
from tkinter import messagebox
from player import Player
from login_manager import LoginManager
from helpers import center


class Login():
    def __init__(self, root, auth, on_logged):
        self.auth = auth
        self.on_logged = on_logged

        self.root = root
        self.root.pack(fill=tk.BOTH, expand=True)
        self.root.configure(bg="light blue")

        self.master = tk.Frame(root)
        self.master.pack(expand=True)
        self.master.configure(bg="light blue")

        lbl = tk.Label(self.master, text='Ласкаво просимо в  гру "Сапер"')
        lbl.grid(row=0, columnspan=2)

        lbl_login = tk.Label(self.master, text='Логін: ')
        self.ent_login = tk.Entry(self.master, width=20)
        lbl_login.grid(row=1, column=0, sticky='e')
        self.ent_login.grid(row=1, column=1)

        lbl_password = tk.Label(self.master, text='Пароль:')
        self.ent_password = tk.Entry(self.master, width=20, show='*')
        lbl_password.grid(row=2, column=0, sticky='e')
        self.ent_password.grid(row=2, column=1)

        btn_login = tk.Button(
            self.master, text='Увійти / Зареєструватися', command=self.__on_login_tap)
        btn_login.grid(row=3, column=0, columnspan=2, sticky='ew')

    def __on_login_tap(self):
        login = self.ent_login.get()
        password = self.ent_password.get()

        if login == '' or password == '':
            messagebox.showerror(
                'Авторизація', 'Поля не можуть бути порожніми')
            return

        res = self.auth.sign_in(login, password)
        if isinstance(res, Player):
            self.on_logged()
        elif isinstance(res, str):
            messagebox.showerror('Авторизація', res)
