import javax.swing.JFrame;

public class SwingExample {

    public static void main(String[] args) {

       // JFrame�N���X�̃C���X�^���X�𐶐� 
        JFrame frame = new JFrame("�v���O���~���O");

        // ����{�^���������̃A�v���P�[�V�����̐U�镑��������
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // �E�B���h�E�̏����T�C�Y�i���C�����j���s�N�Z���P�ʂŐݒ�
        frame.setSize(320, 160);
        // �E�B���h�E�̕\���ꏊ���K��
        frame.setLocationRelativeTo(null);
        // �E�B���h�E��\��
        frame.setVisible(true); 
    } 
}
