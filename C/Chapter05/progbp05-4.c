#include <stdio.h>
/* 関数プロトタイプ */
void sumPointer(int a, int b, int* pSum);

int main() {
  int a = 1;
  int b = 2;
  int sum = 0;

  /* 参照呼出しの関数を実行 */
  sumPointer(a,b,&sum);

  /* sum の値は？ */
  printf("%d + %d = %d !\n", a, b, sum);
  
  return 0;

}

void sumPointer(int a, int b, int* pSum) {

  /* 足し算して値を更新 */
  *pSum = a + b; 

}
