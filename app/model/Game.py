import random

class Game:
    def __init__(self):
        self.id = random.randint(0,999999)
        self.Players = []
        self.AddPlayer()
        return None

    def PlayerCount(self):
        return len(self.Players)

    def AddPlayer(self):
        self.Players.append("")