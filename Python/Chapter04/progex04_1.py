def main():
    # 文字列の初期化
    strPy1 = 'Python';
    print('strPy1 = ' + strPy1)
    # 文字列リストの結合
    strlist = [ 'P', 'y', 't', 'h', 'o', 'n' ]
    strPy2 = ''.join(strlist)
    print('strPy2 = ' + strPy2)
    # 文字の置換
    print("strPy1.replace('o','a') = " 
            + strPy1.replace('o','a'))
    # 小文字への変換
    print('strPy2.lower() = ' + strPy2.lower())
    
if __name__ == '__main__':
    main()
