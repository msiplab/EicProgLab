/*
 * appendix2_2.c
 *
 * プログラミング演習 課題2-2（補足プログラム）
 *
 * 解析解による計算
 * 
 * Copyright (C) 2008-2024, S. Muramatsu
 *
 */

/* 補足プログラム（解析解による計算の）実行例
 *
 * $ gcc appendix2_2.c -o appendix2_2 -lm
 *
 * $ ./appendix2_2 rlcsetup.csv rlcresulthosoku.csv
 * E = 1 [V], R = 1000 [Ohm], L = 0.01 [H], C = 1e-007 [F]
 * t0 = 0 [s], te = 0.001 [s], v = 0 [V], dv/dt = 0, h = 0.01
 * zeta = 1.58114
 * 0.0009999125
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/* 関数プロトタイプ */
void rlccircan(FILE*,FILE*);
double f(double,double);

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
    fprintf(stderr,"%s: ファイルオープンに失敗しました。\n",argv[1]);
    exit(EXIT_FAILURE);
  }

  /* 出力ファイル */
  pfout = fopen(argv[2], "w");
  if ( pfout == NULL ) {
    fprintf(stderr,"%s: ファイルオープンに失敗しました。\n",argv[2]);
    exit(EXIT_FAILURE);
  }

  /* 計算と出力 */
  rlccircan(pfin,pfout);

  /* ファイルクローズ */
  fclose(pfin);
  fclose(pfout);

  return 0;
}

/* RLC回路過渡応答の計算と結果出力 */
void rlccircan(FILE *pfin, FILE *pfout)
{

  /* 変数宣言 */
  double e, r, l, c, h, t, v, dv, te;
  double zeta, tau, x, y, xe;

  /* ファイルからのパラメータの読込 */
  fscanf(pfin, "%lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf, %lf",
	 &e, &r, &l, &c, &t, &te, &v, &dv, &h);

  /* パラメータの確認（標準出力） */
  fprintf(stdout, "E = %g [V], R = %g [Ohm], L = %g [H], C = %g [F]\n",
	  e, r, l, c);
  fprintf(stdout,
	  "t0 = %g [s], te = %g [s], v = %g [V], dv/dt = %g, h = %g\n",
	  t, te, v, dv, h);

  /* 計算の実行とファイル出力 */
  tau = sqrt(l * c);
  zeta = r * c / (2.0*tau);
  fprintf(stdout, "zeta = %g\n", zeta);
  x  = t / tau;  /* x の初期値設定 */
  xe = te / tau; /* x の終了値設定 */
  while (x < xe) {

    /* 解析解による計算 */
    y = f(x,zeta);

    /* 結果出力 */
    t = x * tau;
    v = y * e;
    fprintf(pfout,  "%g, %g\n", t, v); /* 出力ファイルに書込み */
    fprintf(stdout, "%g\r", t);       /* 標準出力に経過表示 */

    /* 更新 */
    x = x + h;

  }
}

/* 解析解による計算 */
double f(double x, double zeta)
{
  double y;
  double sqdz = zeta*zeta;

  if (sqdz > 1)
    y = 1.0 - exp(-zeta*x)*(cosh(sqrt(sqdz-1)*x)
			  + zeta/sqrt(sqdz-1)*sinh(sqrt(sqdz-1)*x));
  else if(sqdz == 1)
    y = 1.0 - (1.0+zeta*x)*exp(-zeta*x);
  else
    y = 1.0 - exp(-zeta*x)*(cos(sqrt(1-sqdz)*x)
			  + zeta/sqrt(1-sqdz)*sin(sqrt(1-sqdz)*x));

  return y;
}
