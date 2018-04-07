#include <stdio.h>
#include <stdlib.h>

/* 要素データの構造定義 */
struct element {
  double data;
  struct element *pNextElement;
};
typedef struct element Element;

/* リストの構造定義 */
typedef struct {
  Element *pHeadElement;
  int length;
} List;

/* 関数プロトタイプ */
void initialize(List*);
void display(List);
void addElement(List*, double);
void removeElement(List*, int);
void insertElement(List*, int, double);

int main() {
  /* リスト型の宣言 */
  List v;
  
  /* 初期化 */
  initialize(&v);

  /* 要素の追加 */
  addElement(&v, 1.0);
  addElement(&v, 2.0);
  addElement(&v, 3.0);
  /* removeElement(&v, 1); */
  /* insertElement(&v, 1, 4.0); */
  
  /* 表示 */
  printf("length = %d\n", v.length); 
  display(v);
	
  return 0;
}

/* ベクトルの初期化 */
void initialize(List *pV) {  
  pV->pHeadElement = NULL;
  pV->length = 0;
}

/* 要素の表示 */
void display(List v) {
  Element *pE;
  pE = v.pHeadElement;
  while(pE != NULL) {
    printf("\t%g\n", pE->data);
    pE = pE->pNextElement;
  }
}

/* 要素の追加 */
void addElement(List *pV, double data) {
  
  /* 最後尾要素のポインタ */
  Element *pLastElement;
  
  /* 新規に追加する要素の生成 */
  Element *pNewElement;
  pNewElement = (Element*)malloc(sizeof(Element));/* 領域確保 */
  pNewElement->data = data;
  pNewElement->pNextElement = NULL;

  if( pV->pHeadElement == NULL ) { /* リストが空の場合 */
    pV->pHeadElement = pNewElement; /* 新規要素を先頭にリンク */
  } else { /* リストが空の場合 */
    pLastElement = pV->pHeadElement;
    while( pLastElement->pNextElement != NULL ) /* 最後尾を探索 */
      pLastElement = pLastElement->pNextElement;
    pLastElement->pNextElement = pNewElement; /* 新規要素を最後尾にリンク */
  }
  pV->length++;
}

/* 要素の削除 */
void removeElement(List *pV, int index) {
  int iElement;
  Element *pEnxtnxt, *pE;
  
  if (index == 0) { /* 先頭の削除 */
    pEnxtnxt = pV->pHeadElement->pNextElement;  
    free(pV->pHeadElement); /* 領域解放 */
    pV->pHeadElement = pEnxtnxt;    
  } else { /* 先頭以外の削除 */
    pE = pV->pHeadElement;  
    for(iElement=0; iElement<index-1; iElement++)
      pE = pE->pNextElement;
    pEnxtnxt = pE->pNextElement->pNextElement;
    free(pE->pNextElement); /* 領域解放 */
    pE->pNextElement = pEnxtnxt;
  }
  pV->length--;
}

/* 要素の挿入 */
void insertElement(List *pV, int index, double data) {
  int iElement;
  Element *pE;

  /* 新規に追加する要素の生成 */
  Element *pNewElement;
  /* 領域確保 */
  pNewElement = 
    (Element*)malloc(sizeof(Element)); 
  pNewElement->data = data;
  pNewElement->pNextElement = NULL;
  if (index >= pV->length) { /* 最後尾への追加 */
    addElement(pV,data);
  } else {
    if (index == 0) { /* 先頭への挿入 */
      pNewElement->pNextElement = pV->pHeadElement;
      pV->pHeadElement = pNewElement;
    } else { /* 先頭以外への挿入 */
      pE = pV->pHeadElement;  
      for(iElement=0; iElement<index-1; iElement++)
	pE = pE->pNextElement;
      pNewElement->pNextElement = pE->pNextElement;
      pE->pNextElement = pNewElement;
    }
    pV->length++;
  }
}
