import java.util.Scanner;
import java.util.Random;

public class Practice4_2 {
    
    public static void main(String args[]) {

	try {			

	    /* 標準入力の準備 */
	    Scanner scanner = new Scanner(System.in);
	    
	    /* 物体形状の選択 */
	    System.out.println(" -- 体積計算プログラム -- ");
	    System.out.println(ThreeDimensionalObjectFactory.getMenu());
	    System.out.print("三次元物体の名称か番号を入力して下さい: ");
	    String name = scanner.next();
	    
	    /* 
	     * 物体名に対応した包含評価のインスタンス生成 
	     * 多相性（ポリモーフィズム）の利用 
	     */
	    IThreeDimensionalObject object3d = 
		ThreeDimensionalObjectFactory.create(name);
	    
	    /* 標本点数の入力 */
	    System.out.print("標本点数を入力して下さい: ");
	    int nSamples = scanner.nextInt();
	    
	    /* 処理の開始 */
	    Random xGenerator = new Random(); // 0 ≦ x ≦ 1
	    Random yGenerator = new Random(); // 0 ≦ y ≦ 1
	    Random zGenerator = new Random(); // 0 ≦ z ≦ 1
	    int nInside = 0;
	    double x, y, z;
	    for(int iSample=0; iSample<nSamples; iSample++) {
		x = xGenerator.nextDouble();
		y = yGenerator.nextDouble();
		z = zGenerator.nextDouble();
		if ( object3d.isInside(x,y,z) )
		    nInside++;
	    }

	    /* 結果の表示 */
	    System.out.println();
	    System.out.println(" " + object3d.getName() + " の体積 ～ " 
			       + 8.0*nInside/nSamples); 
	    System.out.println(" （解析解）" 
			       + object3d.getAnalyticalSolution() );

	} catch (NumberFormatException nfe) {

	    System.err.println(nfe.getMessage());

	} catch (VolumeCalculatorException vce) {

	    System.err.println(vce.getMessage());

	}
    }
}
