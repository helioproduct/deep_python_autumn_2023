import unittest
from io import StringIO
from unittest.mock import patch

from tic_tac_game import TicTacGame, Player, Board, Cell, IncorrectMoveException, Move


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.players = [Player('*'), Player('0')]

    def test_board_update_cell(self):
        board = Board(3)
        board.update_cell(1, 1, '*')
        self.assertEqual(board.data[1][1].symbol, '*')

    def test_cell_is_empty(self):
        cell = Cell()
        self.assertTrue(cell.is_empty())

    def test_cell_update(self):
        cell = Cell()
        cell.update('*')
        self.assertFalse(cell.is_empty())
        self.assertEqual(cell.symbol, '*')


    def test_get_current_player(self):
        game = TicTacGame(self.players, size=3)
        self.assertEqual(game.get_current_player(), self.players[0])
        game.move_number = 1
        self.assertEqual(game.get_current_player(), self.players[1])


    def test_check_winner(self):
        game = TicTacGame(self.players, size=3)
        board = game.board
        board.update_cell(0, 0, '*')
        board.update_cell(1, 1, '*')
        board.update_cell(2, 2, '*')
        move = Move(self.players[0], 2, 2)
        winner = game.check_winner(move)
        self.assertEqual(winner, self.players[0])


if __name__ == '__main__':
    unittest.main()
