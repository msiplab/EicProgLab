#include <stdio.h>
/* 関数プロトタイプ */
void printVector(int*,int);

int main()
{
  int size = 3;
  int a[] = { 1, 2, 3 };

  printVector( a, size );
}

void printVector( int* p, int size )
{
  int i;
  for (i = 0; i<size; i++)
    printf("%d: %d\n",i , *(p+i) );
}
