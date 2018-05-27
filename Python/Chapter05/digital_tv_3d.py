from digital_tv import DigitalTv

class DigitalTv3d(DigitalTv):

    def __init__(self, region):
        # 基底クラスのコンストラクタ
        super().__init__(region)

    def display3d(self, channel):
        if self._region == '新潟':
            if channel == 8:
                print('NHK総合3D表示中...')
            elif channel == 12:
                print('NHK教育3D表示中...')
            else:
                print('3D表示でいません...')
        else:
            print('3D表示できません')

if __name__ == '__main__':

    tv = DigitalTv3d('新潟')
    
    tv.display3d(8)
    tv.display3d(12)
    tv.display3d(1)
    
    tv.display(8)
    tv.display(12)
    tv.display(1)
