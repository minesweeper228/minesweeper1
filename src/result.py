import time


class Result:
    def __init__(self, difficulty, is_win):
        self.date = time.localtime()
        self.difficulty = difficulty
        self.is_win = is_win

    def __repr__(self):
        date = time.strftime('%d.%m %H:%M:%S', self.date)
        return '{} {} ({})'.format(self.is_win, self.difficulty, date)
