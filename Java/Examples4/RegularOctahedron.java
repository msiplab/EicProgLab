public class RegularOctahedron implements IThreeDimensionalObject {

    public boolean isInside(double x, double y, double z) {
	if ( (x + y + z) <= 1.0 )
	    return true;
	else
	    return false;
    }

    public String getName() {
	return "正八面体";
    }

    public double getAnalyticalSolution() {
	return 4.0/3.0;
    }

}
