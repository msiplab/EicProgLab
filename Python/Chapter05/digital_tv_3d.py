from digital_tv import DigitalTv

class DigitalTv3d(DigitalTv):

    def __init__(self, region):
        # 基底クラスのコンストラクタ
        super().__init__(region)
        self.is3d = True

    def display(self, channel):
        if self.is3d == True:
            if self._region == '新潟':
                if channel == 8:
                    print('NHK総合3D表示中...')
                elif channel == 12:
                    print('NHK教育3D表示中...')
                else:
                    print('3D表示できません...')
            else:
                print('3D表示できません')
        else:
            super().display(channel)

if __name__ == '__main__':

    tv = DigitalTv3d('新潟')
    
    tv.display(8)
    tv.display(12)
    tv.display(1)
    
    tv.is3d = False
    
    tv.display(8)
    tv.display(12)
    tv.display(1)
