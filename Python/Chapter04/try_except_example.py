import sys

def main():
    # 名前の入力
    name = input('名前を入力してください> ')
    # 年齢の入力（整数が入力されるまで問い続ける）
    while True:
        try:
            age = int(input('年齢を入力してください> '))
            break
        except ValueError:
            print('年齢には整数を入力してください！')
    # 名前と年齢の表示
    print('名前：{0} （{1:d}歳）'.format(name,age))


if __name__ == '__main__':
    main()
