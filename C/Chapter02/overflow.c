#include <stdio.h>
#define BIG 2000000000

main()
{
    int a, b=BIG, c=BIG;

    a = b + c;
    printf("a=%d b=%d c=%d\n", a, b, c);
}
