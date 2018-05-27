public interface IThreeDimensionalObject {
    boolean isInside(double x, double y, double z);
    String getName();
    double getAnalyticalSolution();
}
