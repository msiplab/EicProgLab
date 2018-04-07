/* 3つの入力データの最大値 */
#include <stdio.h>

int main()
{
  int a, b, c, max;

  scanf("%d%d%d", &a, &b, &c);

  if (b<=a && c<=a) 
    max = a;
  else if (c<=b)
    max = b;
  else 
    max = c;

  printf("max = %d\n", max);
  
  return 0;
}
