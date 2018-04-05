#include <stdio.h>

int f(void); /* 関数プロトタイプ */

int a=1, b=2, c=3; /* 外部変数 */

main()
{
  printf("%3d\n", f());
  printf("%3d%3d%3d\n", a, b, c);
}
