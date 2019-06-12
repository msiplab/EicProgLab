import re

def main():
    # 配列の初期化
    matrix = [ [ 0.0 for irow in range(2) ] for icol in range(2) ]
    # 配列要素の入力  
    for irow in range(2):
        rowvector = input()
        rowelements = re.split('\s*[ ,]\s*', rowvector)
        for icol in range(2):
            matrix[irow][icol] = float(rowelements[icol])
    # 配列要素の転置出力
    for irow in range(2):
        for icol in range(2):
            send = '\n' if icol == 1 else ', '
            print('{0:.2f}'.format(matrix[icol][irow]), end=send)

if __name__ == '__main__':
    main()
