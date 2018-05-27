/*
 * Example3_2.java
 *
 * プログラミング演習　例題3-2（発展）
 *
 * Copyright (c) 2013-2017, Shogo MURAMATSU, All Rights Reserved
 */
public class Example3_2 {

    public static void main(String args[]) {
	MyComplex z0;
	MyComplex z1;
	MyComplex z2;

	/* 引数の数の確認 */
	if(args.length != 4) {
	    System.out.println("引数の数は 4 つ必要です．");
	    System.exit(0);
	}

	/*
         * コマンド引数からのデータの読み込み（C言語の atof に相当）
	 * MyComplex クラスをインスタンス化．
	 */
	z0 = new MyComplex(Double.parseDouble(args[0]),  // 1つめの複素数
			   Double.parseDouble(args[1]));
	z1 = new MyComplex(Double.parseDouble(args[2]),  // 2つめの複素数
			   Double.parseDouble(args[3]));

	/*
	 * 各複素数の内容を表示して確認
	 * System.out.println 引数内で z0 は z0.toString() と等価
	 * System.out.println 引数内で z1 は z1.toString() と等価
	 */
	System.out.println(" z0 \t= " + z0); // 1つめの複素数
	System.out.println(" z1 \t= " + z1); // 2つめの複素数

	/* 符号反転の結果を表示 */
	z2 = z0.negative();                  // 1つめの複素数
	System.out.println("-z0 \t= " + z2);
	z2 = z1.negative();                  // 2つめの複素数
	System.out.println("-z1 \t= " + z2);

	/* 絶対値の結果を表示 */
	System.out.printf("|z0| \t= % g\n", z0.absolute());  // 1つめの複素数
	System.out.printf("|z1| \t= % g\n", z1.absolute());  // 1つめの複素数

	/* 二つの複素数の加算 */
	z2 = z0.plus(z1);
	System.out.println("z0+z1 \t= " + z2);

	/* 二つの複素数の減算 */
	z2 = z0.minus(z1);
	System.out.println("z0-z1 \t= " + z2);

	/* 二つの複素数の積 */
	z2 = z0.multipliedBy(z1);
	System.out.println("z0*z1 \t= " + z2);
    }
}
