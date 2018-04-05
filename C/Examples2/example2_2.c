/*
 * example2_2.c
 *
 * プログラミング演習 例題2-2
 *
 * Copyright (C) 2008-2017, S. Muramatsu
 */
#include <stdio.h>
#include <stdlib.h>

/* 構造体定義 */
typedef struct {
  double x;
  double y;
} State;

/* 関数プロトタイプ */
void rccirc(FILE*,FILE*);
void rceuler(State*,double);
double f(double);

int main(int argc, char *argv[])
{
  /* 変数宣言 */
  FILE *pfin, *pfout;

  /* コマンド引数の数の確認 */
  if ( argc != 3 ) {
    fprintf(stderr,"\t使用法: %s [setup file] [output file]\n",argv[0]);
    exit(EXIT_FAILURE);
  }

  /* 入力ファイル */
  pfin = fopen(argv[1], "r");
  if ( pfin == NULL ) {
    fprintf(stderr,"%s: ファイルオープンに失敗しました．\n",argv[1]);
    exit(EXIT_FAILURE);
  }

  /* 出力ファイル */
  pfout = fopen(argv[2], "w");
  if ( pfout == NULL ) {
    fprintf(stderr,"%s: ファイルオープンに失敗しました．\n",argv[2]);
    exit(EXIT_FAILURE);
  }

  /* 計算と出力 */
  rccirc(pfin,pfout);

  fclose(pfin);
  fclose(pfout);

  return 0;
}

/* RC回路過渡応答の計算と結果出力 */
void rccirc(FILE *pfin, FILE *pfout)
{
  /* 変数宣言 */
  double e, r, c, h, t, v, te, tau, xe;
  State s;

  /* ファイルからのパラメータの読込 */
  fscanf(pfin, "%lf, %lf, %lf, %lf, %lf, %lf, %lf", &e, &r, &c, &t, &te, &v, &h);

  /* パラメータの確認（標準出力） */
  fprintf(stdout, "E = %g [V], R = %g [Ohm], C = %g [F]\n", e, r, c);
  fprintf(stdout, "t = %g [s], te = %g [s], v = %g [V], h = %g\n", t, te, v, h);
  /* 計算の実行とファイル出力 */
  tau = r * c;   /* 時定数の設定 */
  s.x = t / tau;   /* x の初期値設定 */
  s.y = v / e;     /* y の初期値設定 */
  xe = te / tau; /* s.x の終了値設定 */
  while (s.x < xe) {

    /* 結果出力 */
    t = s.x * tau; /* 時刻 t = x_i * τ */
    v = s.y * e;   /* 電圧 v = y_i * E */
    fprintf(pfout,  "%g, %g\n", t, v); /* 出力ファイルに書込み */
    fprintf(stdout, "%g\r", t); /* 標準出力に経過表示 */

    /* Euler法による計算 */
    rceuler(&s, h);
  }
}

/* Euler 法 */
void rceuler(State *ps, double h)
{
  double xnxt, ynxt;

  xnxt = ps->x + h; /* x_{i+1} = x_i + h */
  ynxt = ps->y + h * f(ps->y); /* y_{i+1} = y_i + h*f_i */
  ps->x = xnxt;
  ps->y = ynxt;
}

/* f(x,y) = dy/dx = 1-y */
double f(double y)
{
  return 1.0 - y;
}
