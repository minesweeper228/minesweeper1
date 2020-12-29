from player import Player
from tkinter import messagebox
import pickle
import os


class LoginManager:
    def __init__(self):
        self.__path = 'data.pkl'

        self.cur_player = None
        self.players = []

        try:
            with open(self.__path, 'rb') as f:
                self.players = pickle.load(f)
        except:
            print('"{}" doesn\'t exists'.format(self.__path))

    def __new_player(self, login, password):
        player = Player(login, password)
        self.players.append(player)
        self.__save()
        return player

    def __save(self):
        with open(self.__path, 'wb') as f:
            pickle.dump(self.players, f, pickle.HIGHEST_PROTOCOL)

    def sign_in(self, login, password):
        player = next((player for player in self.players if player.login == login), None)
        if player is not None:
            password_match = player.password == password
            if password_match:
                self.cur_player = player
                return self.cur_player
            else:
                return 'Невірний пароль'
        else:
            if messagebox.askyesno('Авторизація', ' Новий логін: {}, Новий пароль: {}'.format(login, password)):
                self.cur_player = self.__new_player(login, password)
                return self.cur_player
            else:
                return None

    def update_player_results(self, difficulty, is_win):
        self.cur_player.add_result(difficulty, is_win)
        self.__save()

    def get_all_results(self):
        results = []
        for player in self.players:
            results += map(lambda a: (player, a), player.last_results)
        return results
