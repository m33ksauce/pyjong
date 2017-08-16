from app.model.Game import Game

class GameController:
    def __init__(self):
        self.Games = dict()
        return None

    def CreateNewGame(self):
        g = Game()
        self.Games[g.id] = g
        return g
    
    def JoinGame(self, id, player):
        self.Games[id].AddPlayer(player)