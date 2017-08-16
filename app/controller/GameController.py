from app.model.Game import Game

class GameController:
    def __init__(self):
        self.Games = []
        return None

    def CreateNewGame(self):
        g = Game()
        self.Games.append(g)
        return g