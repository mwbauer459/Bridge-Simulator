import random
from time import sleep


class Game:
    top = ""
    bot = ""
    num_players = 0
    rows = 0
    bridge = []
    players = []
    current_player = 1
    current_row = 1

    def __init__(self, players, rows):
        self.num_players = players
        self.rows = rows
        self.make_bridge(rows)
        self.make_players(players)
        self.current_player = 1
        self.current_row = 1

    def make_bridge(self, num):
        for i in range(num):
            x = random.randint(0, 1)
            self.bridge.append(x)

    def make_players(self, num):
        for i in range(num):
            self.players.append(i)

    def take_step(self, row):
        guess = random.randint(0, 1)
        if self.bridge[row] == guess:
            return True
        else:
            return False

    def display_bridge(self, row, state):
        # sleep(1)
        if state:
            if self.bridge[row] == 0:
                self.top += "[]"
                self.bot += " O"
                print(self.top)
                print(self.bot)
            else:
                self.top += " O"
                self.bot += "[]"
                print(self.top)
                print(self.bot)
        else:
            if self.bridge[row] == 0:
                self.top += "[]"
                self.bot += " X"
                print(self.top)
                print(self.bot)
            else:
                self.top += " X"
                self.bot += "[]"
                print(self.top)
                print(self.bot)

    def play_game(self, slurp = False):
        while True:
            state = False
            result = self.take_step(self.current_row)

            if result:
                state = True
                self.display_bridge(self.current_row - 1, state)
                sleep(1)
                self.current_row += 1

            else:
                state = False
                self.display_bridge(self.current_row - 1, state)
                sleep(1)
                print(f'{self.current_player} fell!')
                self.current_player += 1
                self.current_row += 1

            if self.current_player > self.num_players:
                sleep(1)
                print(f'Last player fell on row {self.current_row}')
                break

            if self.current_row >= self.rows:
                sleep(1)
                print(f'First player to make it was {self.current_player}')
                break

        print('Game is over!')

