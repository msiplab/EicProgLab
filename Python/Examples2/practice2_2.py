"""
practice2_2

課題2-2（発展）

Copyright (c) 2023-2024 Shogo MURAMATSU, All rights reserved
"""

import sys
import time
from volume_estimator import VolumeEstimator
from three_dimensional_object_factory import ThreeDimensionalObjectFactory
from volume_calculator_exception import VolumeCalculatorException
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

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
            # プロセス数の入力
            nProcess = int(input('プロセス数を入力して下さい: '))
            # 標本点数の入力
            nSamples = int(input('プロセス毎の標本点数を入力して下さい: '))
            # 総サンプル数の表示
            print('総サンプル数：{0}'.format(nProcess*nSamples))
            # 開始時刻
            start_time = time.time()
            # サブプロセス実行用オブジェクトのインスタンス化
            volest = [ VolumeEstimator(object3d,nSamples) for id in range(nProcess)]
            volacc = 0.0
            with ProcessPoolExecutor() as executor:
                # サブプロセスのスタートとIDの割り当て
                future_volest = { executor.submit(volest[id].run):
                                 id for id in range(nProcess)}
                # サブプロセスの結果の回収
                for future in as_completed(future_volest):
                    id = future_volest[future]
                    volres = future.result()
                    print('{0:02d}:{1:6.4f}'.format(id,volres))
                    volacc += volres
            # 推定の平均値
            volave = volacc/nProcess
            # 処理時間
            elapsed_time = time.time() - start_time
            print('処理時間： {0:6.4f} [s]'.format(elapsed_time))
            # 結果の表示
            print()
            print('{0} の体積 〜 {1}'.format(object3d.name, volave))
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
