import tkinter as tk
from Menu import Menu
from Login import Login
from helpers import center, update_window_size
from login_manager import LoginManager
from Game import Game
from results_table import ResultsTable

auth = LoginManager()

window = None
root = None


def end_game(diff_str, result):
    auth.update_player_results(diff_str, result)
    configure_menu()


def start_game(diff_str):
    global root
    if diff_str == 'новачок':
        update_window_size(window, 800, 450)
    elif diff_str == 'любитель':
        update_window_size(window, 800, 500)
    else:
        update_window_size(window, 1000, 500)
    root.destroy()
    root = tk.Frame()
    root.pack()
    Game(root, diff_str, end_game)


def results():
    global root, auth
    ResultsTable(root, auth)


def configure_menu():
    global root
    update_window_size(window, 800, 450)
    root.destroy()
    root = tk.Frame()
    Menu(root, start_game, results, configure_game)


def configure_game():
    global root
    update_window_size(window, 800, 450)
    if root is not None:
        root.destroy()
    root = tk.Frame()
    Login(root, auth, configure_menu)


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Сапер')
    center(window)

    configure_game()

    window.mainloop()
