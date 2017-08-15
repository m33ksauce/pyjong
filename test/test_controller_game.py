import unittest
from app.controller.game import GameController, Game

class TestGameController(unittest.TestCase):

    def test_create_unique_game(self):
        gc = GameController()
        game1 = gc.NewGame()
        self.assertIsInstance(game1, Game)
        game2 = gc.NewGame()
        self.assertIsInstance(game2, Game)
        self.assertNotEqual(game1.id, game2.id)

    def test_GameController_has_game_list(self):
        gc = GameController()
        self.assertTrue(hasattr(gc, "Games"))

    def test_Game_added_to_GameController(self):
         gc = GameController()
         game1 = gc.NewGame()
         self.assertEqual(len(gc.Games), 1)
         self.assertEqual(game1.id, gc.Games[0].id)
