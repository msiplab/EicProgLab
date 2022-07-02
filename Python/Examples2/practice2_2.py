import sys
from three_dimensional_object_factory import ThreeDimensionalObjectFactory
from volume_calculator_exception import VolumeCalculatorException
from random import random

def main(args):
    while True:
        try:
            # 物体形状の選択
            print(' –- 体積計算プログラム -- ')
            print(ThreeDimensionalObjectFactory.get_menu())
            name = input('三次元物体の名称か番号を入力して下さい： ')
            # 物体名に対応した包含評価のインスタンス生成
            # 多態性（ポリモーフィズム）の利用
            object3d = ThreeDimensionalObjectFactory.create(name)
            # 標本点数の入力
            nSamples = int(input('標本点数を入力して下さい: '))
            # 処理の開始 
            nInside = 0
            for iSample in range(nSamples):
                x = 2.0*(random()-0.5) # [-1,1]
                y = 2.0*(random()-0.5) # [-1,1]
                z = 2.0*(random()-0.5) # [-1,1]
                if object3d.is_inside(x,y,z):
                    nInside += 1
            # 結果の表示
            vol = 8.0*nInside/nSamples
            print()
            print('{0} の体積 〜 {1}'.format(object3d.name, vol))
            print('(解析解) {0}'.format(object3d.analytical_solution))
        except ValueError as ve:
            print(ve)
        except VolumeCalculatorException as vce:
            print(vce)
        # プログラム継続の問い合わせ
        ans = input('継続しますか？ [y]：')
        if ans != 'y' and ans != 'Y':
            break

if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
