public class ProgEx8_1 {
    /* ルート3の定義 （定数は static final）*/
    static final double SQRT_OF_3 = 1.73205080756888;
    /* main メソッド */
    public static void main(String args[]) {
	if (args.length != 1) {
	    System.out.println("エラー:引数の数 " + args.length );
	} else {
	    /* 変数宣言 */
	    double l; /* 一辺の長さ */
	    double area;   /* 正三角形の面積 */
	    /* コマンド引数からのデータの読み込み（C言語の atof に相当）*/
	    l = Double.parseDouble(args[0]);
	    
	    /* 面積の計算(底辺d×高さ/2) */
	    area = l * (SQRT_OF_3 / 2.0 * l) / 2.0;
	    
	    /* 正三角形の面積の表示 */
	    System.out.println("一辺の長さが " + l + " の正三角形の面積");
	    System.out.println("     = " + area);
	}
    }
}
