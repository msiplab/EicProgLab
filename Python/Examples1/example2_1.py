import othello

def main():
    try:
        board = othello.Board()
        
        board.displayState()
        
        print('(x,y) = (3,4)')
        board.tryPlaceStone(3,4)
        
        board.displayState()
        
        print('(x,y) = (5,3)')
        board.tryPlaceStone(5,3)
        
        board.displayState()
        
        print('パス')
        board.change()
        
        board.displayState()
        
    except othello.BoardOutOfRangeException as boore:
        print()
        print(boore)
        
    
if __name__ == '__main__':
    main()
