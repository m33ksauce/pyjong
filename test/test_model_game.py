import unittest
from app.model.Game import Game
from app.model.Player import Player

class TestGameModel(unittest.TestCase):
    
    def test_Game_does_not_start_with_less_than_four_players(self):
        game = Game()
        self.assertFalse(game.Started)

    def test_Game_can_start_with_four_players(self):
        game = Game()
        player = Player()
        game.AddPlayer(player)
        game.AddPlayer(player)
        game.AddPlayer(player)
        game.AddPlayer(player)
        game.Start()
        self.assertEqual(game.PlayerCount(), 4)
        self.assertTrue(game.Started)

    def test_Game_player_can_join_game(self):
        game = Game()
        player = Player()
        self.assertTrue(game.AddPlayer(player))