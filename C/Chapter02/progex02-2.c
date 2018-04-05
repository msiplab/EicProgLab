#include <stdio.h>

main()
{
  int c;
  while ((c = getchar()) != EOF)
    if ('a' <= c && c <= 'z')
      putchar(c - 'a' + 'A');
    else
      putchar(c);
}
