from typing import List


class Cell:

    def __init__(self, symbol=None):
        self.symbol = symbol
        self.empty = True
        if self.symbol:
            self.empty = False

    def is_empty(self):
        return self.empty

    def update(self, symbol):
        self.symbol = symbol
        self.empty = False
    

    def __str__(self) -> str:
        if self.is_empty():
            return ' '
        return self.symbol


class Player:

    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

class Move:

    def __init__(self, player: Player, column: int, row: int):
        self.player = player
        self.column = column
        self.row = row


class IncorrectMoveException(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class CeilIsOccupiedException(Exception):
    def __init__(self, message=None):
        pass


class Board:

    def __init__(self, size=3):
        self.size = size
        self.data = [[Cell() for _ in range(size)] for _ in range(size)]

    def show(self):

        # show column
        print(end=' ')
        for i in range(self.size):
            print(i, end=' ')
        print('\r')

        for i in range(self.size):
            # show row
            print(i, end='')
            for j in range(self.size):
                print(self.data[i][j], end=' ')
            print('\r')

    def update_cell(self, column: int, row: int, symbol):
        self.data[column][row].update(symbol)


class TicTacGame:

    def __init__(self, players: List[Player], size=3):
        self.players = players
        self.move_number = 0
        self.size = size
        self.board = Board(size)

    def get_current_player(self) -> Player:
        return self.players[self.move_number % len(self.players)]

    def show_game(self):
        print(f"\n{self.get_current_player()} move:")
        self.board.show()

    def parse_input(self) -> Move:
        try:
            column = int(input("Enter column: "))
            row = int(input("Enter row: "))
        except ValueError as e:
            raise e
        if column >= self.size or row >= self.size:
            raise IncorrectMoveException()
        return Move(self.get_current_player(), column, row)

    def game_cycle(self):

        while True:
            self.show_game()

            while True:
                try:
                    move = self.parse_input()
                    if self.board.data[move.column][move.row].is_empty():
                        break
                    else:
                        print('Move is not available. Сell is occupied')
                except:
                    print(f'Enter integers <= {self.size}')

            self.board.update_cell(move.column, move.row, move.player.symbol)
            self.move_number += 1
            
            winner = self.check_winner()
            if winner:
                print(f"{winner} won!")
                break

    def start_game(self):
        print('TIC TAC GAME')
        self.game_cycle()


    def check_winner(self):
        return self.players[0]
        pass


game = TicTacGame(size=3, players=[Player('*'), Player('0')])
game.start_game()

