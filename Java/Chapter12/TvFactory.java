public class TvFactory {

    static ITv createTv(String tvSpec) 
    	throws TvException {

	if (tvSpec.equals("�v���Y�}"))
	    return new PlasmaTv();
	else if (tvSpec.equals("�t��"))
	    return new LcdTv();
	else
	    throw new TvException(
		tvSpec + " �͗��p�s�D");
    }
}
