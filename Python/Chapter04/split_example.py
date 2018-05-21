def main():
    # 文字列（文章）
    sentence = 'Rome was not built in a day.'
    # 単語リスト（空白区切り）
    words = sentence.split(' ')
    # 単語の表示
    for idx in range(len(words)):
        print('{0:d}: {1}'.format(idx,words[idx]))

if __name__ == '__main__':
    main()

