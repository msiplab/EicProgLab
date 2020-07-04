from cat import Cat

def main():
    tama = Cat(name='タマ', weight=10, favorite='マグロ')
    mike = Cat(name='ミケ', favorite='サンマ')
    
    print(tama.name + 'の体重：' + str(tama.weight) + 'kg')
    print(mike.name + 'の体重：' + str(mike.weight) + 'kg')
    
    tama.feed('マグロ')
    tama.feed('マグロ')
    tama.feed('マグロ')
    tama.feed('サンマ')
    mike.feed('マグロ')
    mike.feed('サンマ')
    
    print(tama.name + 'の体重：' + str(tama.weight) + 'kg')
    print(mike.name + 'の体重：' + str(mike.weight) + 'kg')


if __name__ == '__main__':
    main()
