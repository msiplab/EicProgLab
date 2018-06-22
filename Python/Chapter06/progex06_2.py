import numpy as np

def main():
    # 行列Aの定義
    A = np.array( [ [1, 1], [1, -1] ] )
    # ベクトルbの定義
    b = np.array( [ 1, 2] )
    # ベクトルxの解
    x = np.linalg.solve(A, b)
    print(x)
    
if __name__ == '__main__':
    main()
    
