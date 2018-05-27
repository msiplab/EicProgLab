class DigitalTv:
    
    def __init__(self,region):
        self._region = region
        
    def display(self,channel):
        if self._region == '新潟':
            if channel == 8:
                print('NHK総合表示中...')
            elif channel == 12:
                print('NHK教育表示中...')
            else:
                print('受信できません...')
        else:
            print('受信できません')


if __name__ == '__main__':
    
    tv = DigitalTv('新潟')
    
    tv.display(8)
    tv.display(12)
    tv.display(1)
