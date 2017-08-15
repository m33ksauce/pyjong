import random

class GameController:
    def __init__(self):
        self.Games = []
        return None

    def NewGame(self):
        g = Game()
        self.Games.append(g)
        return g

class Game:
    def __init__(self):
        self.id = random.randint(0,999999)
        return None