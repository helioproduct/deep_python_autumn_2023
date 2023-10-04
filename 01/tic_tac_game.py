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


class Board:
    def __init__(self, size=3):
        self.size = size
        self.data = [[Cell() for _ in range(size)] for _ in range(size)]

    def show(self):
        # Print column numbers
        print("  ", end="")
        for i in range(self.size):
            print(i, end=" ")
        print()

        for i in range(self.size):
            # Print row number
            print(i, end=" ")
            for j in range(self.size):
                print(self.data[i][j], end=" ")
            print()

    def update_cell(self, column: int, row: int, symbol):
        self.data[row][column].update(symbol)


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

        if column < 0 or column >= self.size or row < 0 or row >= self.size:
            raise IncorrectMoveException(
                f"Invalid input. Enter valid integers between 0 and {self.size - 1}.")
        return Move(self.get_current_player(), column, row)

    def game_cycle(self):
        while True:
            self.show_game()

            while True:
                try:
                    move = self.parse_input()
                    cell = self.board.data[move.row][move.column]

                    if cell.is_empty():
                        cell.update(move.player.symbol)
                        self.move_number += 1
                        break
                    else:
                        print('Cell is occupied. Please choose another cell.')
                except KeyboardInterrupt:
                    print("\nGame terminated by user.")
                    exit(0)
                except (ValueError, IncorrectMoveException):
                    print(
                        f'Enter valid integers between 0 and {self.size - 1}.')

            winner = self.check_winner(move)
            if winner:
                self.show_game()
                print(f'{winner} wins!')
                break
            elif self.move_number == self.size ** 2:
                self.show_game()
                print('It\'s a draw!')
                break

    def start_game(self):
        print('TIC TAC GAME')
        self.game_cycle()

    def check_winner(self, move: Move):
        symbol = move.player.symbol

        # Проверка по горизонтали
        for i in range(self.size):
            if all(self.board.data[i][j].symbol == symbol for j in range(self.size)):
                return move.player

        # Проверка по вертикали
        for j in range(self.size):
            if all(self.board.data[i][j].symbol == symbol for i in range(self.size)):
                return move.player

        # Проверка по диагоналям
        if all(self.board.data[i][i].symbol == symbol for i in range(self.size)) or \
                all(self.board.data[i][self.size - 1 - i].symbol == symbol
                    for i in range(self.size)):
            return move.player

        return None


if __name__ == '__main__':

    game = TicTacGame(size=3, players=[Player('*'), Player('0')])
    game.start_game()
