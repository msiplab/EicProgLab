import re

def main():
    # 配列の初期化
    matrix = [ [ 0 for irow in range(3) ] for icol in range(3) ]
    # 配列要素の入力
    print('3x3行列の要素を入力して下さい:')    
    for irow in range(3):
        rowvector = input()
        rowelements = re.split('\s+', rowvector)
        for icol in range(3):
            matrix[irow][icol] = float(rowelements[icol])
    # 配列要素の出力
    print('3x3行列の要素は，')
    for irow in range(3):
        for icol in range(3):
            print('{0:} '.format(matrix[irow][icol]), end='')
        print()


if __name__ == '__main__':
    main()
