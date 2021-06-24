"""
example2_1

例題2-1（基礎）

Copyright (c) 2018-2021 Shogo MURAMATSU, All rights reserved
"""
from board import Board
from board_out_of_range_exception import BoardOutOfRangeException

def main():
    try:
        # Board型のインスタンスboardを生成
        board = Board() 
        # 盤(board)の状態を表示（初期状態）
        board.display_state()
        # 盤(board)の3列4行目に手番の石(Black)を置いてみる
        print('(x,y) = (3,4)')
        board.try_place_stone(3,4)
        # 盤(board)の状態を表示
        board.display_state()
        # 現在のスコアの表示
        display_current_score(board)
        # 現在の手番の石の表示
        display_current_stone(board)
        print()
        
        # 盤(board)の5列3行目に手番の石(White)を置いてみる
        print('(x,y) = (5,3)')
        board.try_place_stone(5,3)
        # 盤(board)の状態を表示
        board.display_state()
        # 現在のスコアの表示
        display_current_score(board)
        # 現在の手番の石の表示
        display_current_stone(board)
        print()
        
        # パスする
        print('パス')
        board.change()
        # 盤(board)の状態を表示
        board.display_state()
        # 現在のスコアの表示
        display_current_score(board)
        # 現在の手番の石の表示
        display_current_stone(board)
        print()
        
        # コマンド入力待ち
        input('\n終了します [Enter]')
        
    except BoardOutOfRangeException as boore:
        print()
        print(boore)
        
def display_current_score(board: Board):
    """現在のスコアの表示"""
    nw = board.number_of_white_cells
    nb = board.number_of_black_cells
    ne = board.number_of_empty_cells
    print('現在のスコア： 白 {0}, 黒 {1}, 空 {2}'.format(nw,nb,ne))

def display_current_stone(board: Board):
    """現在の手番の石の表示"""
    print('現在の手番：',end='')
    if board.current_stone == Board.BLACK:
        print('黒(B)')
    else:
        print('白(W)')     
    
if __name__ == '__main__':
    main()
