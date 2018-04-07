#include <stdio.h>
#include <string.h>

int main()
{
  char str1[] = "string";
  char str2[] = { 's','t','r','i','n','g','\0'};

  printf("str1 = %s\n",str1);
  printf("str2 = %s\n",str2);

  if(strcmp(str1,str2)==0)
    printf("str1 と str2 は同じ文字列です。\n");
  else
    printf("str1 と str2 は異る文字列です。\n");
  
  return 0;

}
