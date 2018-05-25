import sys
def main(args):
    try:
        nom = int(args[1])  # 分子の読込み
        den = int(args[2])  # 分母の読込み
        print('{0:d}/{1:d} = {2:d} 余り {3:d}'.format(
                nom, den, nom//den, nom%den))
    except ZeroDivisionError:
        print('ゼロ割が発生しました。')
    except IndexError:
        print('引数が足りません。')
    except ValueError:
        print('整数ではありません。')
    else:
        print('例外処理は発生しませんでした。')
    finally:
        print('finallyブロックは必ず実行されます。')


if __name__ == '__main__':
    main(sys.argv)
