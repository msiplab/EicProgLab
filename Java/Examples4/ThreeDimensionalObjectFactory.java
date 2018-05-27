public class ThreeDimensionalObjectFactory {

    public static String getMenu() {
	String menu = " 1. 球\n" +
	              " 2. 正八面体";
	return menu;
    }

    public static IThreeDimensionalObject create(String name) 
	throws VolumeCalculatorException {
	if( name.equals("1") || name.equals("球") ) {    		
	    return new Sphere();
    	} else if( name.equals("2") || name.equals("正八面体") ) {
	    return new RegularOctahedron();    	
    	} else {    		
	    throw new VolumeCalculatorException(
		   name + " は無効です．" );
	}
    }
}
