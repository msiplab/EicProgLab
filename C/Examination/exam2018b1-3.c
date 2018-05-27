#include <stdio.h>

double f(double);
double g(double);
double h(double);

double y = 2.0;

int main(){
  printf("(a) % 6.2f \n", f(2.0));
  printf("(b) % 6.2f \n", g(2.0));
  printf("(c) % 6.2f \n", h(2.0));
  y = -4.0;
  printf("(d) % 6.2f \n", f(4.0));
  printf("(e) % 6.2f \n", g(4.0));
  printf("(f) % 6.2f \n", h(4.0));
  return 0;
}

double f(double x) {
  double y = 0.0;
  y = y + x;
  return y;
}

double g(double x) {
  static double y = 0.0;
  y = y + x;
  return y;
}

double h(double x) {
  y = y + x;
  return y;
}
