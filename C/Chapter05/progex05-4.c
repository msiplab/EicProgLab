#include <stdio.h>
/* 関数プロトタイプ */
void sumValue(int a, int b, int sum); 

int main() {
  int a = 1;
  int b = 2;
  int sum = 0;

  /* 値呼出しの関数を実行 */
  sumValue(a,b,sum);

  /* sum の値は？ */
  printf("%d + %d = %d ?\n", a, b, sum);
  
  return 0;

}

void sumValue(int a, int b, int sum) {
  
  /* 足し算して値を更新 */
  sum = a + b; 

}
