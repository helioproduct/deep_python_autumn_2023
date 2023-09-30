
class Cell:

    def __init__(self, symbol=None):
        self.symbol = symbol
        self.empty = True
        if self.symbol:
            self.empty = False
    
    def is_empty(self):
        return self.empty


    def __str__(self) -> str:
        if self.is_empty():
            return ' '
        return self.symbol

class Board:
    
    def __init__(self, size=3):
        self.size = size
        self.data = [[Cell() for _ in range(size)] for _ in range(size)]
        

    def show(self): 
        
        self.data[0][0] = Cell('*')
        self.data[2][2] = Cell('0')
        self.data[1][1] = Cell('+')

        # show column
        print(end=' ')
        for i in range(self.size):
            print(chr(ord('A') + i), end=' ')
        print('\r')

        for i in range(self.size):
            # show row
            print(i + 1, end='')
            for j in range(self.size):
                print(self.data[i][j], end=' ')
            print('\r')



class TicTacGame:

    def __init__(self, size=3, players=['✖', '0']):
        self.players = players
        self.current_player = players[0]    
        self.board = Board(size)

    def show_game(self):
        print(f"{self.current_player}'move:")
        self.board.show()

    def input():
        int(input("Column = "))
        pass

    def start_game(self):
        pass

    def check_winner():
        pass


# board = Board()
# board.show()


game = TicTacGame()
game.show_game()




