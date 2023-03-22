import random

class Board:
    def __init__(self) -> None:
        self.board = [
                [' ',' ',' '],
                [' ',' ',' '],
                [' ',' ',' ']
                ]

    def print_board(self)->None:
        print("\n ~~~~~~~~~~~~~ ")
        for r in self.board:
            print(end=" | ")
            for x in r:
                print(x,end=" | ")
            print("\n ~~~~~~~~~~~~~ ")
        print()

    def check_win(self,sym) -> bool:
        for i in range(3):
            if sym == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if sym == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if sym == self.board[0][0] == self.board[1][1] == self.board[2][2]: return True
        if sym == self.board[0][2] == self.board[1][1] == self.board[2][0]: return True
        return False
        
    def check_draw(self) -> bool:
        spcheck = 0
        for r in self.board:
            if ' ' in r:
                spcheck +=1
        return not spcheck

    def verify_and_update(self,x,y,sym) -> bool:
        if self.board[x][y] == ' ':
            self.board[x][y] = sym
        else:
            return False
        return True

    def reset(self) -> None:
        self.board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
    
    def rmloser(self,sym) -> None:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == sym: self.board[i][j] = ' '

def game():
    SYMBOLS = ['X','O']
    mode = int(input("PvP(0) or PvC(1): "))
    if mode == 1:
        PLAYERS = SYMBOLS
        mv = 0
    else:
        PLAYERS = [SYMBOLS.pop(random.randint(0,1)),SYMBOLS[0]]
        mv = random.randint(0,1)
    
    b = Board()
    while True:
        while True:
            currPL = PLAYERS[mv%2]
            print(f"{currPL}'s Move!")
            mv+=1
            b.print_board()
            if currPL == PLAYERS[0]:
                while True:
                    r, c = int(input(f"Enter the row for {currPL}: ")),int(input(f"Enter the column for {currPL}: "))
                    if b.verify_and_update(r,c,currPL):
                        break
                    print("Enter a valid empty position!")
            else:
                while True:
                    if b.verify_and_update(random.randint(0,2),random.randint(0,2),currPL):
                        break
            if b.check_win(currPL):
                print(f"{currPL} Wins!")
                b.rmloser(PLAYERS[mv%2])
                b.print_board()
                print("Good Game!!")
                break
            if b.check_draw():
                print("Draw Match!!")
                b.print_board()
                print("Good Game!")
                break
        if 'y' != input("Wanna Play again? (y/n): ").lower():
            break
        else:
            b.reset()
if __name__ == '__main__':
    game()

