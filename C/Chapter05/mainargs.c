#include <stdio.h>
/* 端末上でコマンド引数を渡して実行 */

int main( int argc, char *argv[] ) {
  
  int i;

  for (i=0; i<argc; i++)
    printf("%d: %s\n", i, argv[i]);
  
  return 0;

}
