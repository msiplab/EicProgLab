public class ExceptionExample {

    public static void main(String args[]) {
    
	try {
            int nom = Integer.parseInt(args[0]); // ���q�̓Ǎ���
	    int den = Integer.parseInt(args[1]); // ����̓Ǎ���
            System.out.println(nom + "/" + den + " = " + nom/den 
			       + " �]�� " + nom%den);
        } catch(ArithmeticException ae) { 
            // �[�����̗�O
            System.out.println("�Z�p���Z�Ɏ��s���܂���");
        } catch(ArrayIndexOutOfBoundsException aiobe) { 
            // �����͈͂𒴂�����O
            System.out.println("�z��͈̔͂𒴂��܂���");
        } catch(NumberFormatException nfe) {
            // �����̃~�X�}�b�`�̗�O
            System.out.println("���l�f�[�^�ł͂���܂���");
        } finally {
            System.out.println("finally�͕K�����s�����u���b�N�ł�");
        }
    }
		  
}
