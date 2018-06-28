import time
from concurrent.futures import ThreadPoolExecutor

def main():
    # スレッドオブジェクトのインスタンス化
    calro = CiaoThread('Calro',2.0)
    maria = CiaoThread('Maria',1.0)
    with ThreadPoolExecutor(max_workers=2) as executor:
        # スレッドスタート
        executor.submit(calro.run)
        executor.submit(maria.run)

class CiaoThread():
    
    def __init__(self, name, sleeptime):
        self.__name = name
        self.__sleeptime = sleeptime

    def run(self):
        for i in range(10):
            time.sleep(self.__sleeptime)
            print(self.__name + ': Ciao!')
            
if __name__ == '__main__':
    main()
