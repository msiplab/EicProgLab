#include <stdio.h>

int fauto(int);   /* 関数プロトタイプ */
int fstatic(int); 

main()
{
  int a = 1;

  printf("auto  : %d\n", fauto(a));
  printf("static: %d\n", fstatic(a));

  printf("auto  : %d\n", fauto(a));
  printf("static: %d\n", fstatic(a));
}

int fauto(int a)
{
  int s = 0;
  s += a;
  return s;
}

int fstatic(int a)
{
  static int s = 0;
  s += a;
  return s;
}