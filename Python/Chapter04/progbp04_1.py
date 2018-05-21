import sys

def main(args):
    # args の内容を表示
    print('内容　：',args)
    # args のタイプを表示
    print('タイプ：',type(args))
    # args の要素数を表示
    print('要素数：',len(args))
    # 最初の要素にアクセス
    print('-- head --')
    print('args[0]：', args[0])
    # 最後の要素にアクセス
    print('-- tail --')
    print('args[-1]：', args[-1])
    # 最後に要素を追加(append)
    args.append('append')
    print('-- append --')
    print('内容：', args)
    # 途中に要素を挿入
    args.insert(1,'insert')
    print('-- insert --')
    print('内容：', args)
    # 指定位置の要素を抽出(pop)
    last = args.pop(-1)
    print('-- pop --')
    print('last = ：', last)
    print('内容：', args)
    # 指定の値の要素を削除(remove)
    args.remove('insert')
    print('-- insert --')
    print('内容：', args)
    # リストの連結
    print('-- newlist --')
    newlist = args + ['Niigata', 'Univ.']
    print('内容：', newlist)
    # リストの部分アクセス（スライス）
    print('-- slice --')
    print('newlist[1:3] = ', newlist[1:3])
    # リストの並べ替え
    newlist.sort()
    print('-- sort --')
    print('内容：', newlist)
    # リストの反転
    newlist.reverse()
    print('-- reverse --')
    print('内容：', newlist)


if __name__ == '__main__':

    main(sys.argv)
