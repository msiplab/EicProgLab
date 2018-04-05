#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPS 1.0e-15  /* 収束判定値 */
#define MAX_ITER 100 /* 最大反復回数 */ 

double f(double);  /* 関数 */
double df(double); /* 導関数 */

main(int argc, char *argv[])
{
  double xpre;  /* 更新前の値 */
  double xnxt = atof(argv[1]); /* 更新後の値（初期化）*/
  int iIter = 0; /* 反復回数 */
  
  do { 
    printf("x_{%03d} = %21.16g\n", iIter, xnxt);
    xpre = xnxt; 
    xnxt = xpre - f(xpre)/df(xpre); /* ニュートン法 */
     if (iIter >= MAX_ITER) {
      printf("%3d 回の反復で収束しませんでした．\n",
                 iIter);
      break;
    }
  iIter++;
  } while( fabs(xnxt-xpre) > EPS ); /* 収束判定 */
}

double f(double x) /* 関数 */
{
  return 0.5-x+0.2*sin(x);
}

double df(double x) /* 導関数 */
{
  return -1.0+0.2*cos(x);
}

