#include <stdio.h>

void call_by_value(int); /* 関数プロトタイプ */
void call_by_reference(int*);

int main()
{
    int a=1;
 
    printf("%d\n", a);
    call_by_value(a); /* 値呼出し */
    printf("%d\n", a); /* a の値は不変！*/
    call_by_reference(&a); /* 参照呼出し */
    printf("%d\n", a); /* a の値は変わる！ */
}

void call_by_value(int a)
{
    a = 777;
}

void call_by_reference(int *a)
{
    *a = 777;
}
