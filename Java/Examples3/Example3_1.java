/**
 * Example3_1.java
 *
 * プログラミング演習　例題3-1（基礎）
 *
 * (c) Copyright 2007-2017, Shogo MURAMATSU, All rights reserved
 */
public class Example3_1 {

    /* ルート3の定義 （定数は static final）*/
    static final double SQRT_OF_3 = 1.73205080756888;

    /* main メソッド */
    public static void main(String args[]) {

	if (args.length != 1) {

	    System.out.println("エラー:引数の数 " + args.length );

	} else {

	    /* 変数宣言 */
	    double ell;    // 一辺の長さ
	    double area;   // 正三角形の面積

	    /* コマンド引数からのデータの読み込み（C言語の atof に相当）*/
	    ell = Double.parseDouble(args[0]);

	    /* 面積の計算(底辺×高さ/2) */
	    area = ell * (SQRT_OF_3 / 2.0 * ell) / 2.0;

	    /* 正三角形の面積の表示 */
	    System.out.println("一辺の長さが " + ell + " の正三角形の面積");
	    System.out.println("     = " + area);
	}
    }
}
