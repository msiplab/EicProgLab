public class ExtendsExample {

    public static void main(String args[]) {

	DigitalTv digitalTv;
	DigitalTv3d digitalTv3d;

	/* �X�[�p�[�i�e�j�N���X */
	digitalTv = new DigitalTv("�V��");
	digitalTv.display(8);

	/* �T�u�i�q�j�N���X */
	digitalTv3d = new DigitalTv3d("�V��");
	digitalTv3d.display(8);
	digitalTv3d.display3d(8);

    }
}
