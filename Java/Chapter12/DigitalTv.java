public class DigitalTv {
    String _region;

    public DigitalTv(String region){
	_region = region;
    }

    public void display(int channel) {
	if (_region.equals("新潟") ) {
	    switch (channel) {
	    case 8:
		System.out.println("NHK総合表示中...");
		break;
	    case 12:
		System.out.println("NHK教育表示中...");
		break;
	    default:
		System.out.println("受信できません...");
		break;
	    }
	}
	else
	    System.out.println("受信できません");
	
    }
}
