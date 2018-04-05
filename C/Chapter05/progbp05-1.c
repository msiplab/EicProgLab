#include <stdio.h>
void sub(void); /* 関数プロトタイプ */

int a = 1;

int main()
{
    int  a = 22;
    printf("(1) %d\n", a);
    {
        int  a = 333;
        printf("(2) %d\n", a);
    }
    printf("(3) %d\n", a);
    sub();
}


void sub(void)
{
    int  b = 4444;
    printf("(4) %d\n", a);
    printf("(5) %d\n", b);
}
