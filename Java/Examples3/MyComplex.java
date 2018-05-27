/*
 * MyComplex.java
 *
 * プログラミング演習　例題3-2（発展）
 *
 * Copyright (c) 2013-2017, Shogo MURAMATSU, All Rights Reserved
 */
public class MyComplex {

    private double _real;
    private double _imag;

    /* コンストラクタ */
    public MyComplex(double real, double imag) {
	this._real = real;
	this._imag = imag;
    }

    /* 複素数の表示 */
    public String toString() {
	String sgn = ( this._imag < 0 ) ? " - j" : " + j";
	String str = new String(this._real + sgn + Math.abs(this._imag));
	return str;
    }

    /* 複素数の符号反転演算 */
    public MyComplex negative(){
	MyComplex result;
	result = new MyComplex( -this._real, -this._imag );
	return result;
   }

    /* 複素数の絶対値 */
    public double absolute() {
	double result;
	result = Math.sqrt( (this._real*this._real)
			   + (this._imag*this._imag) );
	return result;
    }

    /* 複素数の加算 */
    public MyComplex plus(MyComplex another) {
	MyComplex result;
	result = new MyComplex( this._real + another._real,
				this._imag + another._imag );
	return result;
    }

    /* 複素数の減算*/
    public MyComplex minus(MyComplex another) {
	MyComplex result;
	result = new MyComplex( this._real - another._real,
				this._imag - another._imag );
	return result;
    }

    /* 複素数の積算 */
    public MyComplex multipliedBy(MyComplex another ) {
	MyComplex result;
	result = new MyComplex( this._real * another._real
				- this._imag * another._imag,
				this._real * another._imag
				+ this._imag * another._real);
	return result;
    }
}
