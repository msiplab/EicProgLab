public class PeopleListeningToMusic {
    
    public static void main(String args[]) {
	
	/* Person ���C���X�^���X�� */
	Person taro = new Person("���Y", "�A�j��");
	Person hanako = new Person("�Ԏq", "�A�C�h��");

	/* Cd ���C���X�^���X�� */
	Cd animeCd = new Cd("�A�j��");

	/* CdPlayer ���C���X�^���X�� */
	CdPlayer panasonyPlayer = new CdPlayer();
       
	/* panasonyPlayer �� animeCd ���Z�b�g */
	panasonyPlayer.setCd(animeCd);

	/* taro �� hanako �� Cd �𕷂����� */
	taro.listenToMusic(panasonyPlayer);
	hanako.listenToMusic(panasonyPlayer);

	/* taro �� hanako �̋C���́H */
	System.out.println("���Y�̋C���F " + taro.kibun);
	System.out.println("�Ԏq�̋C���F " + hanako.kibun);
    }
}
