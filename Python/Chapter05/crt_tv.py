from interface_tv import ITv

class CrtTv(ITv):
    def __init__(self):
        pass
    
    def display(self,channel):
        print('ブラウン管：', end='')
        if self.__region == '新潟':
            if channel == 8:
                print('NHK総合表示中...')
            elif channel == 12:
                print('NHK教育表示中...')
            else:
                print('表示できません...')
        else:
            print('表示できません')    
    
    
    @property
    def region(self):
        return self.__region
        
    
    @region.setter
    def region(self,value):
        self.__region = value
    

def main():
    assert issubclass(CrtTv().__class__, ITv)
    assert isinstance(CrtTv(), ITv)
    
    tv = CrtTv()
    tv.region = '新潟'
    tv.display(8)


if __name__ == '__main__':
    main()
