import junit.framework.TestCase;

public class ComplexTest extends TestCase {

    /* ���Z�e�X�g */
    public void testAdd() {

	/* �C���X�^���X�� */
	Complex z0 = new Complex(1,2);
	Complex z1 = new Complex(3,4);
	Complex z2;

	/* ���Z�̎��s */
	z2 = z0.add(z1);

	/* ���Ғl */
	double realExpctd = 4;
	double imagExpctd = 6;

	/* �����l */
	double realActual = z2.getReal();
	double imagActual = z2.getImag();
	
	/* �]�� */
	assertEquals(realExpctd, realActual);
	assertEquals(imagExpctd, imagActual);
    }

    /* ���Z�e�X�g */
    public void testSub() {

	/* �C���X�^���X�� */
	Complex z0 = new Complex(1,2);
	Complex z1 = new Complex(3,4);
	Complex z2;

	/* ���Z�̎��s */
	z2 = z0.sub(z1);

	/* ���Ғl */
	double realExpctd = -2;
	double imagExpctd = -2;

	/* �����l */
	double realActual = z2.getReal();
	double imagActual = z2.getImag();
	
	/* �]�� */
	assertEquals(realExpctd, realActual);
	assertEquals(imagExpctd, imagActual);
    }

}
