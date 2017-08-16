import unittest
from app.controller.GameController import GameController
from app.model.Game import Game
from app.model.Player import Player

class TestGameController(unittest.TestCase):

    def test_GameController_create_unique_game(self):
        gc = GameController()
        game1 = gc.CreateNewGame()
        self.assertIsInstance(game1, Game)
        game2 = gc.CreateNewGame()
        self.assertIsInstance(game2, Game)
        self.assertNotEqual(game1.id, game2.id)

    def test_GameController_has_game_list(self):
        gc = GameController()
        self.assertTrue(hasattr(gc, "Games"))

    def test_GameController_game_added_to_GameController(self):
         gc = GameController()
         game1 = gc.CreateNewGame()
         self.assertEqual(len(gc.Games), 1)
         self.assertEqual(game1.id, gc.Games[game1.id].id)

    def test_GameController_player_can_join_Game_by_ID(self):
        gc = GameController()
        game = gc.CreateNewGame()
        player = Player()
        gc.JoinGame(game.id, player)
        self.assertIn(player, gc.Games[game.id].Players)
    
    def test_GameController_player_cannot_join_game_with_more_than_4_players(self):
        gc = GameController()
        game = gc.CreateNewGame()
        player = Player()
        gc.JoinGame(game.id, player)
        gc.JoinGame(game.id, player)
        gc.JoinGame(game.id, player)
        gc.JoinGame(game.id, player)
        # should have 4 players
        self.assertEqual(gc.Games[game.id].PlayerCount(), 4)
        with self.assertRaises(GameFullError):
            gc.JoinGame(game.id, player)
        
