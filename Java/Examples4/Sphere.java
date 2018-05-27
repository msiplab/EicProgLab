public class Sphere implements IThreeDimensionalObject {

    public boolean isInside(double x, double y, double z) {
	if ( (x*x + y*y + z*z) <= 1.0 )
	    return true;
	else 
	    return false;
    }

    public String getName() {
	return "球";
    }

    public double getAnalyticalSolution() {
	return Math.PI*4.0/3.0;
    }

}
