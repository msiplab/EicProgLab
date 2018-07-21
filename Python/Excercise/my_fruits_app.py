from fruits_factory import FruitsFactory

def main():
    names = [ 'Goya', 'Suika', 'Lemon' ]
    
    for iFruit in range(len(names)):
        fruit = FruitsFactory.create(names[iFruit])
        print(fruit.name + ': ',end='')
        print(fruit.taste)


if __name__ == '__main__':
    main()
