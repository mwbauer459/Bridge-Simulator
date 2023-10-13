import random

class Game:
    top = ""
    bot = ""
    num_players = 0
    rows = 0
    bridge = []
    players = []

    def __init__(self, players, rows):
        self.num_players = players
        self.rows = rows
        self.make_bridge(rows)
        self.make_players(players)

    def make_bridge(self, num):
        for i in range(num):
            x = random.randint(0, 1)
            self.bridge.append(x)

    def make_players(self, num):
        for i in range(num):
            self.players.append(i)

    def take_step(self, bridge, row):
        guess = random.randint(0, 1)
        if bridge[row] == guess:
            return True
        else:
            return False

    def display_bridge(self, bridge, row, state):
        if state:
            if bridge[row] == 0:
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
            if bridge[row] == 0:
                self.top += "[]"
                self.bot += " X"
                print(self.top)
                print(self.bot)
            else:
                self.top += " X"
                self.bot += "[]"
                print(self.top)
                print(self.bot)
