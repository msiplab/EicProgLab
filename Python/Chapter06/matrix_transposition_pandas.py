# 予め Pandas をインストール
# $ sudo apt-get install python3-pandas
import pandas as pd 
import sys

def main(args):
    # 配列要素の入力 
    df = pd.read_csv(args[1], header=None)
    # 配列要素の転置
    df = df.transpose()
    # 配列要素の出力
    df.to_csv(args[2], header=None, index=None)
                
if __name__ == '__main__':
    main(sys.argv)
