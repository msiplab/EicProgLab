public class DigitalTv3d extends DigitalTv {

    public DigitalTv3d(String region) {
	super(region); // �e�N���X�̃R���X�g���N�^
    }

    public void display3d(int channel) {  
	if (_region.equals("�V��") ) {
	    switch (channel) {
	    case 8:
		System.out.println("NHK����3D�\����...");
		break;
	    case 12:
		System.out.println("NHK����3D�\����...");
		break;
	    default:
		System.out.println("3D�\���ł��܂���...");
		break;
	    }
	}
	else
	    System.out.println("3D�\���ł��܂���");
    }
}
