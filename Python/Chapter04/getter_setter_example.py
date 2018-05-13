import sys
    
def main():
    
    dog = Dog('マサル') # インスタンス化
    
    dog.weight = 10.   # 正の実数をセット
    print(dog.name + 'の体重は', dog.weight, 'kg')
    
    dog.weight = -10.    # 負の実数をセット
    print(dog.name + 'の体重は', dog.weight, 'kg')
    
class Dog:
    """Dogクラス"""
    
    def __init__(self,name):
        """コンストラクタ"""
        self.__name   = name
        self.__weight = 0.
        
    @property
    def name(self):
        """nameゲッター"""
        return self.__name
        
    @property
    def weight(self):
        """weightゲッター"""
        return self.__weight
        
    @weight.setter
    def weight(self,weight):
        """weightセッター"""
        if isinstance(weight,float) and weight > 0:
            self.__weight = weight
        else:
            print('エラー：体重は正の実数',file=sys.stderr)    
            sys.exit(0)    

if __name__ == '__main__':
    
    main()

