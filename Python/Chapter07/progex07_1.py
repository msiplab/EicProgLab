import time
from concurrent.futures import ThreadPoolExecutor

def main():
    # スレッド実行用オブジェクトのインスタンス化
    calro = Ciao('Calro',2.0)
    maria = Ciao('Maria',1.0)
    with ThreadPoolExecutor(max_workers=2) as executor:
        # スレッドスタート
        executor.submit(calro.run)
        executor.submit(maria.run)

class Ciao():
    
    def __init__(self, name, sleeptime):
        """コンストラクタ"""
        self.__name = name
        self.__sleeptime = sleeptime

    def run(self):
        """あいさつメソッド"""
        for i in range(10):
            time.sleep(self.__sleeptime)
            print(self.__name + ': Ciao!')
            
if __name__ == '__main__':
    main()
