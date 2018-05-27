public class FactoryExample {

    public static void main(String args[]) {
	ITv tv;
	String tvSpec = args[0];
	String region = args[1];
	int channel = Integer.parseInt(args[2]);

	try {
	    tv = TvFactory.createTv(tvSpec);
	    tv.setRegion(region);
	    tv.display(channel);
	} catch (TvException te) {
	    System.out.println(te.getMessage());
	}
    }

}

