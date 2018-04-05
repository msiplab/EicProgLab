#include <stdio.h>

main()
{
  float a = 6144.006835937500f;
  float b = 6144.005859375000f;
  float c;

  c = a - b;

  printf("a = %21.18e\n",a);
  printf("b = %21.18e\n",b);
  printf("c = %21.18e\n",c);
}
