public class LcdTv implements ITv {
    private String _region;

    public void setRegion(String region) {
	_region = region;
    }

    public void display(int channel) {
	if (_region.equals("�V��") ) {
	    switch (channel) {
	    case 8:
		System.out.println("LCD: NHK�����\����...");
		break;
	    case 12:
		System.out.println("LCD: NHK����\����...");
		break;
	    default:
		System.out.println("��M�ł��܂���...");
		break;
	    }
	}
	else
	    System.out.println("��M�ł��܂���");
	
    }
}
