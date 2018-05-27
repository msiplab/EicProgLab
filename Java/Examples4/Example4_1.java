/*
 * Example4_1.java
 * 
 * 例題4-1（基礎）
 * 
 * Copyright (c) 2006-2015, Shogo MURAMATSU, All Rights Reserved
 */

public class Example4_1 {
    public static void main(String args[]) {
	
    	try {
    		/* Board型の変数boardを宣言 */
    		Board board = new Board();
	    
    		/* 盤(board)の状態を表示（初期状態） */
    		board.displayState();

    		/* 盤(board)の3列4行目に手番の石(Black)を置いてみる */
    		System.out.println("(x,y) = (3,4)");
    		board.tryPlaceStone(3, 4);
    		/* 盤(board)の状態を表示 */
    		board.displayState();
    		
    		/* 盤(board)の5列3行目に手番の石(White)を置いてみる */
    		System.out.println("(x,y) = (5,3)");
    		board.tryPlaceStone(5, 3);
    		/* 盤(board)の状態を表示 */
    		board.displayState();    		

    		/* パスする */
    		System.out.println("パス");
    		board.pass();
    		/* 盤(board)の状態を表示 */
    		board.displayState(); 

    		System.out.println();

    	} catch (BoardOutOfRangeException boore) {
    		System.out.println(boore.getMessage());
    	}
    }
}
