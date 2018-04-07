#include <stdio.h>

int main()
{
  /* 変数宣言 */
  int n;	/* 近似次数 */
  double x, y = 1.0; /* 独立変数、従属変数 */
  
  /* 途中の計算に必要な変数の宣言 */	
  int i; /* 繰り返し変数の宣言 */
  double f = 1.0, p = 1.0; /* 階乗値，累乗値 */
  
  /* データの読み込み(倍精度, 整数) */
  scanf("%lf%d",&x,&n);
  
  for (i=1; i<=n; i++) {
    f *= (double)i; 
    p *= x; 
    y +=  p / f; 
  }	
  
  /* e^x の近似値の表示 */
  printf("マクローリン展開による次数 %d までの e^(%g) の近似値\n"
	 "    =%21.16g\n", n, x, y);

  return 0;

}
