from my_string_stack import MyStringStack

def main():
    stackSize = 5
    movies = MyStringStack(stackSize)

    movies.pushdown('ジュラシック・ワールド')
    movies.pushdown('劇場版ポケットモンスター')
    movies.pushdown('ハン・ソロ')

    print('{0:d}: {1}'.format(\
        movies.top,movies.popup()))
    print('{0:d}: {1}'.format(\
        movies.top,movies.popup()))

    movies.pushdown('万引き家族')
    movies.pushdown('空飛ぶタイヤ')

    print('{0:d}: {1}'.format(\
        movies.top,movies.popup()))
    print('{0:d}: {1}'.format(\
        movies.top,movies.popup()))
    print('{0:d}: {1}'.format(\
        movies.top,movies.popup()))

if __name__ == '__main__':
    main()
