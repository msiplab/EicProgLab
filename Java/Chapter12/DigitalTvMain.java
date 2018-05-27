public class DigitalTvMain {

    public static void main(String args[]) {

	DigitalTv digitalTv;
	String region = "êVäÉ";

	digitalTv = new DigitalTv(region);
	digitalTv.display(8);

	digitalTv = new DigitalTv3d(region);
	digitalTv.display(12);
	((DigitalTv3d)digitalTv).display3d(12);

    }
}
