public class ProgEx8_1 {
    /* ���[�g3�̒�` �i�萔�� static final�j*/
    static final double SQRT_OF_3 = 1.73205080756888;
    /* main ���\�b�h */
    public static void main(String args[]) {
	if (args.length != 1) {
	    System.out.println("�G���[:�����̐� " + args.length );
	} else {
	    /* �ϐ��錾 */
	    double l; /* ��ӂ̒��� */
	    double area;   /* ���O�p�`�̖ʐ� */
	    /* �R�}���h��������̃f�[�^�̓ǂݍ��݁iC����� atof �ɑ����j*/
	    l = Double.parseDouble(args[0]);
	    
	    /* �ʐς̌v�Z(���d�~����/2) */
	    area = l * (SQRT_OF_3 / 2.0 * l) / 2.0;
	    
	    /* ���O�p�`�̖ʐς̕\�� */
	    System.out.println("��ӂ̒����� " + l + " �̐��O�p�`�̖ʐ�");
	    System.out.println("     = " + area);
	}
    }
}
