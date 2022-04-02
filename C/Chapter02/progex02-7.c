#include <stdio.h>

int main()
{
  int c;
  /* Ctrl-d で終了 */
  while ((c = getchar()) != EOF)
    if ('a' <= c && c <= 'z')
      putchar(c - 'a' + 'A');
    else
      putchar(c);
  return 0;
}
