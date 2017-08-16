import random

class Game:
    def __init__(self):
        self.id = random.randint(0,999999)
        self.Players = []
        self.Started = False
        return None

    def PlayerCount(self):
        return len(self.Players)

    def AddPlayer(self, p):
        self.Players.append(p)
        return True

    def Start(self):
        if self.PlayerCount() == 4:
            self.Started = True
        return self.Started