"""
practice2_2

課題2-2（発展）

Copyright (c) 2024-2025 Shogo MURAMATSU, All rights reserved
"""

import sys
import time
from expectation_estimator import ExpectationEstimator
from probability_density_function_factory import ProbabilityDensityFunctionFactory
from expectation_estimator_exception import ExpectationEstimatorException
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

def main(args):
    while True:
        try:
            # 2変量関数の選択
            print(' –- 期待値計算プログラム -- ')
            print(ProbabilityDensityFunctionFactory.get_menu())
            name = input('確率密度関数の番号を入力して下さい： ')
            # 確率密度関数名に対応したインスタンス生成
            # 多態性（ポリモーフィズム）の利用
            pdf = ProbabilityDensityFunctionFactory.create(name)
            # 確率密度関数のパラメータ入力
            pdf.parameter_inquiry()
            # プロセス数の入力
            nProcess = int(input('プロセス数を入力して下さい: '))
            # 標本点数の入力
            nSamples = int(input('プロセス毎の標本点数を入力して下さい: '))
            # 総サンプル数の表示
            print('総サンプル数：{0}'.format(nProcess*nSamples))
            # 開始時刻
            start_time = time.time()
            # サブプロセス実行用オブジェクトのインスタンス化
            expest = [ ExpectationEstimator(pdf,nSamples) for id in range(nProcess)]
            expacc = 0.0
            with ProcessPoolExecutor() as executor:
                # サブプロセスのスタートとIDの割り当て
                future_expest = { executor.submit(expest[id].run):
                                 id for id in range(nProcess)}
                # サブプロセスの結果の回収
                for future in as_completed(future_expest):
                    id = future_expest[future]
                    expres = future.result()
                    print('{0:02d}:{1:6.4f}'.format(id,expres))
                    expacc += expres
            # 推定の平均値
            expave = expacc/nProcess
            # 処理時間
            elapsed_time = time.time() - start_time
            print('処理時間： {0:6.4f} [s]'.format(elapsed_time))
            # 結果の表示
            print()
            print('{0} の期待値 〜 {1}'.format(pdf.name, expave))
            print('(解析解) {0}'.format(pdf.analytical_expectation))
        except ValueError as ve:
            print(ve)
        except ExpectationEstimatorException as vce:
            print(vce)
        # プログラム継続の問い合わせ
        ans = input('継続しますか？ [y]：')
        if ans != 'y' and ans != 'Y':
            break

if __name__ == '__main__':
    main(sys.argv)
    sys.exit(0)
