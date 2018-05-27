/*
 * Example3_2.java
 *
 * �v���O���~���O���K�@���3-2�i���W�j
 *
 * Copyright (c) 2013-2017, Shogo MURAMATSU, All Rights Reserved
 */
public class Example3_2 {

    public static void main(String args[]) {
	MyComplex z0;
	MyComplex z1;
	MyComplex z2;

	/* �����̐��̊m�F */
	if(args.length != 4) {
	    System.out.println("�����̐��� 4 �K�v�ł��D");
	    System.exit(0);
	}

	/*
         * �R�}���h��������̃f�[�^�̓ǂݍ��݁iC����� atof �ɑ����j
	 * MyComplex �N���X���C���X�^���X���D
	 */
	z0 = new MyComplex(Double.parseDouble(args[0]),  // 1�߂̕��f��
			   Double.parseDouble(args[1]));
	z1 = new MyComplex(Double.parseDouble(args[2]),  // 2�߂̕��f��
			   Double.parseDouble(args[3]));

	/*
	 * �e���f���̓��e��\�����Ċm�F
	 * System.out.println �������� z0 �� z0.toString() �Ɠ���
	 * System.out.println �������� z1 �� z1.toString() �Ɠ���
	 */
	System.out.println(" z0 \t= " + z0); // 1�߂̕��f��
	System.out.println(" z1 \t= " + z1); // 2�߂̕��f��

	/* �������]�̌��ʂ�\�� */
	z2 = z0.negative();                  // 1�߂̕��f��
	System.out.println("-z0 \t= " + z2);
	z2 = z1.negative();                  // 2�߂̕��f��
	System.out.println("-z1 \t= " + z2);

	/* ��Βl�̌��ʂ�\�� */
	System.out.printf("|z0| \t= % g\n", z0.absolute());  // 1�߂̕��f��
	System.out.printf("|z1| \t= % g\n", z1.absolute());  // 1�߂̕��f��

	/* ��̕��f���̉��Z */
	z2 = z0.plus(z1);
	System.out.println("z0+z1 \t= " + z2);

	/* ��̕��f���̌��Z */
	z2 = z0.minus(z1);
	System.out.println("z0-z1 \t= " + z2);

	/* ��̕��f���̐� */
	z2 = z0.multipliedBy(z1);
	System.out.println("z0*z1 \t= " + z2);
    }
}
