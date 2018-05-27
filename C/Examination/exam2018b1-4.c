#include <stdio.h>
#include <math.h>

typedef struct {
  char c;
  double x;
  double y;
} Point;

void display(Point p);
void move(Point* pp, double dx, double dy);
double distance(Point p0, Point p1);

int main() {
  Point pointa = { 'A', 1.0, 1.0 };
  Point pointb = { 'B', 0.0, 2.0 };
  double d;
  
  display(pointa);
  display(pointb);
  move(&pointb, -2.0, 3.0);
  display(pointb);
  d = distance(pointa, pointb);
  printf("点 %c と点 %c の距離： % 4.2f\n",
    pointa.c, pointb.c, d);
  return 0;
}

void display(Point p) {
  printf("点 %c の位置：　(% 4.2f, % 4.2f)\n",
    p.c, p.x, p.y);
}

void move(Point* pp, double dx, double dy) {
  pp->x += dx;
  pp->y += dy;
}

double distance(Point p0, Point p1) {
  double dx = (p0.x - p1.x);
  double dy = (p0.y - p1.y);
  return sqrt(dx*dx + dy*dy);
}
