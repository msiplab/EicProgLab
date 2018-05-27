public class DigitalTv3d extends DigitalTv {

    public DigitalTv3d(String region) {
	super(region); // 親クラスのコンストラクタ
    }

    public void display3d(int channel) {  
	if (_region.equals("新潟") ) {
	    switch (channel) {
	    case 8:
		System.out.println("NHK総合3D表示中...");
		break;
	    case 12:
		System.out.println("NHK教育3D表示中...");
		break;
	    default:
		System.out.println("3D表示できません...");
		break;
	    }
	}
	else
	    System.out.println("3D表示できません");
    }
}
