public class RcCircMain {
    
    public static void main(String args[]) {

        /* �ϐ��錾�Ɛݒ� */
        double e = 1.0;     /* 1.0[V] */
        double r = 1.0e3;   /* 1.0[k��] */
        double c = 0.1e-6;  /* 0.1[��F] */
        double t = 0.0;     /* 0.0[ms] �J�n���� */    
        double te = 1.0e-3; /* 1.0[ms] �I������ */
        double v = 0.0;     /* v0 = 0.0[V] �������� */
        double h = 0.01;
        double tau, x, y, xe;
	
        /* �v�Z�̎��s�ƕW���o�� */
        tau = r * c;   /* ���萔�̐ݒ� */
        x = t / tau;   /* x �̏����l�ݒ� */
        y = v / e;     /* y �̏����l�ݒ� */
        xe = te / tau; /* x �̏I���l�ݒ� */
        RcCircEuler rceuler  = new RcCircEuler(tau,x,y);
        while (rceuler.getX() < xe) {
            t = rceuler.getX() * tau; /* ���� t = x_i * �� */
            v = rceuler.getY() * e;   /* �d�� v = y_i * E */
            System.out.printf("%g %g\n", t, v); /* �W���o�� */
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
