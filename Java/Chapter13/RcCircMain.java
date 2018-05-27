public class RcCircMain {
    
    public static void main(String args[]) {

        /* 変数宣言と設定 */
        double e = 1.0;     /* 1.0[V] */
        double r = 1.0e3;   /* 1.0[kΩ] */
        double c = 0.1e-6;  /* 0.1[μF] */
        double t = 0.0;     /* 0.0[ms] 開始時刻 */    
        double te = 1.0e-3; /* 1.0[ms] 終了時刻 */
        double v = 0.0;     /* v0 = 0.0[V] 初期条件 */
        double h = 0.01;
        double tau, x, y, xe;
	
        /* 計算の実行と標準出力 */
        tau = r * c;   /* 時定数の設定 */
        x = t / tau;   /* x の初期値設定 */
        y = v / e;     /* y の初期値設定 */
        xe = te / tau; /* x の終了値設定 */
        RcCircEuler rceuler  = new RcCircEuler(tau,x,y);
        while (rceuler.getX() < xe) {
            t = rceuler.getX() * tau; /* 時刻 t = x_i * τ */
            v = rceuler.getY() * e;   /* 電圧 v = y_i * E */
            System.out.printf("%g %g\n", t, v); /* 標準出力 */
            rceuler.update(h);
        } 
    }
}

class RcCircEuler{
    
    private double _tau;
    private double _x;
    private double _y;
    
    RcCircEuler(double tau, double x, double y){
        _tau = tau;
        _x = x;
        _y = y;
    }
    
    double getX() { return _x; }
    double getY() { return _y; }
    
    void update(double h) {
        double xnxt, ynxt;
        xnxt = _x + h; /* x_{i+1} = x_i + h */
        ynxt = _y + h * f(_y); /* y_{i+1} = y_i + h*f_i */
        _x = xnxt; /* i=i+1 */
        _y = ynxt;
    }
    
    private double f(double y) { /* f(x,y) = dy/dx = 1-y */            
        return 1.0 - y;
    }
}
