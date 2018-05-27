public class ExtendsExample {

    public static void main(String args[]) {

	DigitalTv digitalTv;
	DigitalTv3d digitalTv3d;

	/* スーパー（親）クラス */
	digitalTv = new DigitalTv("新潟");
	digitalTv.display(8);

	/* サブ（子）クラス */
	digitalTv3d = new DigitalTv3d("新潟");
	digitalTv3d.display(8);
	digitalTv3d.display3d(8);

    }
}
