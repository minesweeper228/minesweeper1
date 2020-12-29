from result import Result


class Player:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.last_results = []

    def add_result(self, difficulty, is_win):
        self.last_results.insert(0, Result(difficulty, is_win))
        self.last_results = self.last_results[:10]
