import time
from concurrent.futures import ProcessPoolExecutor

def main():
    # プロセス実行用オブジェクトのインスタンス化
    calro = Ciao('Calro',2.0)
    maria = Ciao('Maria',1.0)
    with ProcessPoolExecutor(max_workers=2) as executor:
        # プロセススタート
        executor.submit(calro.run)
        executor.submit(maria.run)

class Ciao():
    
    def __init__(self, name, sleeptime):
        self.__name = name
        self.__sleeptime = sleeptime

    def run(self):
        for i in range(10):
            time.sleep(self.__sleeptime)
            print(self.__name + ': Ciao!')
            
if __name__ == '__main__':
    main()
