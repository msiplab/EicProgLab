public class InterfaceExample {

    public static void main(String args[]) {
	ITv tv;
	String tvSpec = args[0];
	String region = args[1];
	int channel = Integer.parseInt(args[2]);

	try {
	    if (tvSpec.equals("�v���Y�}"))
		tv = new PlasmaTv();
	    else if (tvSpec.equals("�t��"))
		tv = new LcdTv();
	    else 
		throw new TvException(
		    tvSpec + " �͗��p�s�D");
	    tv.setRegion(region);
	    tv.display(channel);
	} catch (TvException te) {
	    System.out.println(te.getMessage());
	}
    }

}

