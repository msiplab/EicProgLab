#include <stdio.h>
#define SQRT_OF_3 1.73205080756888 /* ルート３のマクロ定義 */

int main() 
{
  /* 変数宣言 */
  double length; /* 一辺の長さ */
  double area;   /* 正三角形の面積 */
  
  /* データの読み込み(倍精度) */
  scanf("%lf", &length);
  
  /* 面積の計算(底辺×高さ/2) */
  area = length * (SQRT_OF_3 / 2.0 * length) / 2.0;
  
  /* 正三角形の面積の表示 */
  printf("一辺の長さが %f の正三角形の面積\n   = %f\n",
	 length, area);

}
