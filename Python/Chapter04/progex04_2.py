import sys

def main():
    # 標準出力
    sys.stdout.write('Input a character: ')
    sys.stdout.flush()
    # 標準入力
    c = sys.stdin.read(1)
    sys.stdout.write("character '" + c 
                        + "' has a code number "
                        + str(ord(c)) + '.\n')
    sys.stdout.flush()
    # 標準エラー
    sys.stderr.write('Finish!')
    
if __name__ == '__main__':
    main()
