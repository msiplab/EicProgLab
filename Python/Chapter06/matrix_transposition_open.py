import re
import sys

def main(args):
    # 配列の初期化
    matrix = [ [ 0.0 for irow in range(2) ] for icol in range(2) ]
    # 配列要素の入力 
    with open(args[1], 'r') as f:
        for irow in range(2):
            rowvector = f.readline()
            rowelements = re.split('\s*,?\s*', rowvector)
            for icol in range(2):
                matrix[irow][icol] = float(rowelements[icol])
    # 配列要素の転置出力
    with open(args[2], 'w') as f:
        for irow in range(2):
            for icol in range(2):
                send = '\n' if icol == 1 else ', '
                f.write('{0:.2f}'.format(matrix[icol][irow])+send)
                
if __name__ == '__main__':
    main(sys.argv)
