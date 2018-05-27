import junit.framework.TestCase;

public class ComplexTest extends TestCase {

    /* 加算テスト */
    public void testAdd() {

	/* インスタンス化 */
	Complex z0 = new Complex(1,2);
	Complex z1 = new Complex(3,4);
	Complex z2;

	/* 加算の実行 */
	z2 = z0.add(z1);

	/* 期待値 */
	double realExpctd = 4;
	double imagExpctd = 6;

	/* 実測値 */
	double realActual = z2.getReal();
	double imagActual = z2.getImag();
	
	/* 評価 */
	assertEquals(realExpctd, realActual);
	assertEquals(imagExpctd, imagActual);
    }

    /* 減算テスト */
    public void testSub() {

	/* インスタンス化 */
	Complex z0 = new Complex(1,2);
	Complex z1 = new Complex(3,4);
	Complex z2;

	/* 加算の実行 */
	z2 = z0.sub(z1);

	/* 期待値 */
	double realExpctd = -2;
	double imagExpctd = -2;

	/* 実測値 */
	double realActual = z2.getReal();
	double imagActual = z2.getImag();
	
	/* 評価 */
	assertEquals(realExpctd, realActual);
	assertEquals(imagExpctd, imagActual);
    }

}
