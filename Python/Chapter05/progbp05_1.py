def main():
    tama = Cat('タマ', 'マグロ', 10)
    mike = Cat('ミケ', 'サンマ', 5)
    
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
    
class Cat:
    
    def __init__(self, name, favorite, weight):
        self.__name = name
        self.__favorite = favorite
        self.__weight = weight
    
    def feed(self, food):
        if self.__favorite == food:
            self.__weight += 1
            
    @property
    def name(self):
        return self.__name
    
    @property
    def weight(self):
        return self.__weight    
    
if __name__ == '__main__':
    main()
