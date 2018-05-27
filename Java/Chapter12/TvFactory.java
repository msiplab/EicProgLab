public class TvFactory {

    static ITv createTv(String tvSpec) 
    	throws TvException {

	if (tvSpec.equals("プラズマ"))
	    return new PlasmaTv();
	else if (tvSpec.equals("液晶"))
	    return new LcdTv();
	else
	    throw new TvException(
		tvSpec + " は利用不可．");
    }
}
