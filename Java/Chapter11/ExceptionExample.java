public class ExceptionExample {

    public static void main(String args[]) {
    
	try {
            int nom = Integer.parseInt(args[0]); // 分子の読込み
	    int den = Integer.parseInt(args[1]); // 分母の読込み
            System.out.println(nom + "/" + den + " = " + nom/den 
			       + " 余り " + nom%den);
        } catch(ArithmeticException ae) { 
            // ゼロ割の例外
            System.out.println("算術演算に失敗しました");
        } catch(ArrayIndexOutOfBoundsException aiobe) { 
            // 引数範囲を超えた例外
            System.out.println("配列の範囲を超えました");
        } catch(NumberFormatException nfe) {
            // 引数のミスマッチの例外
            System.out.println("数値データではありません");
        } finally {
            System.out.println("finallyは必ず実行されるブロックです");
        }
    }
		  
}
