#include <stdio.h>
#include <math.h>

#define EPS 10E-15

double newtonupdate(double*);
double f(double); /* 関数 */
double df(double); /* 導関数　*/

int main(){
  double x = 0.0;
  double err;
  
  err = newtonupdate(&x);
  while(err > EPS)
    err = newtonupdate(&x);
  
  printf("x = % 6.4f\n", x);
}

/* ニュートン法の更新と誤差評価 */
double newtonupdate(double* px) {
  double err; /* 更新前後の誤差 */
  double xpre; /* 更新前の値 */
  double xnxt; /* 更新後の値 */
  
  xpre = *px;
  xnxt = xpre - f(xpre)/df(xpre);
  err = fabs(xnxt - xpre);
  /* (c) 値の更新 */
  *px = xnxt;
  
  return err;
}

/* (b) 関数 f の定義 */
double f(double x){
  return 100.0-exp(-x);
}

/* (c) 導関数 df の定義 */
double df(double x){
  return exp(-x);
}
