#include <stdio.h>
#include <stdlib.h>

void rceuler(double*,double*,double);
double f(double);

main()
{
  /* 変数宣言と設定 */
  double e = 1.0;       /*　E= 1.0[V] */
  double r = 1.0e3;   /* R=1.0[kΩ] */
  double c = 0.1e-6;  /* C=0.1[μF] */
  double t = 0.0;       /* t0=0.0[ms] 開始時刻 */    
  double te = 1.0e-3; /* te=1.0[ms] 終了時刻 */
  double v = 0.0;       /* v0 = 0.0[V] 初期条件 */
  double h = 0.01;
  double tau, x, y, xe;
  
  /* 計算の実行と標準出力 */
  tau = r * c;   /* 時定数の設定 */
  x = t / tau;   /* x の初期値設定 */
  y = v / e;     /* y の初期値設定 */
  xe = te / tau; /* x の終了値設定 */  
while (x < xe) {
    t = x * tau; /* 時刻 t = x_i * τ */
    v = y * e;   /* 電圧 v = y_i * E */
    fprintf(stdout,  "%g, %g\n", t, v); /* 標準出力 */
    rceuler(&x, &y, h);
  } 
}

/* オイラー法 */
void rceuler(double *px, double *py, double h)
{
  double xnxt, ynxt;
  
  xnxt = *px + h; /* x_{i+1} = x_i + h */
  ynxt = *py + h * f(*py); /* y_{i+1} = y_i + h*f_i */
  *px = xnxt; /* i=i+1 */
  *py = ynxt;
}

/* f(x,y) = dy/dx = 1-y */ 
double f(double y) 
{
  return 1.0 - y;
}
