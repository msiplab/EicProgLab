def main():
    
    name = input('名前を入力して下さい> ')
    
    age = int(input('年齢を入力して下さい> '))
    
    print('名前：{0} （{1:d}歳）'.format(name,age))

if __name__ == '__main__':
    main()
