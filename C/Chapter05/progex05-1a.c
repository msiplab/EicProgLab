#include <stdio.h>
/* ビルドは端末上で以下のコマンドを実行 
 * 
 * $ gcc -Wall progex05-1a.c progex05-1b.c -o progex05-1
 * 
 * 実行は端末上で以下のコマンドを実行
 * 
 * $ ./progex05-1
 * 
 */

int f(void); /* 関数プロトタイプ */

int a=1, b=2, c=3; /* 外部変数 */

int main()
{
  printf("%3d\n", f());
  printf("%3d%3d%3d\n", a, b, c);
}
