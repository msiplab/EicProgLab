from random_string import RandomString

def main():
    itemlist = [ 'グー', 'チョキ', 'パー' ]
    """a"""
    randstr = RandomString(itemlist)
    ntrials = 4
    print('リスト: ',end='')
    for iitem in range(len(itemlist)):
        print('{0} '.format(randstr.get_item_at(iitem)),end='')
    print()
    print('試行')
    for itrial in range(ntrials):
        print('{0:d}:{1}'.format(itrial,randstr.next()))

if __name__ == '__main__':
    main()
