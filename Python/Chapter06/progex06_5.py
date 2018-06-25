import sys
from random import randint

MIN = 1
MAX = 6

def main(args):
    
    try:
        # サンプル数の取得
        nSamples = int(args[1])
        # 擬似乱数の生成と表示
        for iSample in range(nSamples):
            print(randint(MIN,MAX))
    except IndexError as ie:
        print('引数の数が足りません', file=sys.stderr)
        
if __name__ == '__main__':
    main(sys.argv)
