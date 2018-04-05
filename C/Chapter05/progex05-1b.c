/* ビルドは端末上で以下のコマンドを実行 
 * 
 * $ gcc -Wall progex05-1a.c progex05-1b.c -o progex05-1
 * 
 * 実行は端末上で以下のコマンドを実行
 * 
 * $ ./progex05-1
 * 
 */
 
 int f(void)
{
  extern int a;
  int b, c;

  a=b=c=4;
  return a+b+c;
}
