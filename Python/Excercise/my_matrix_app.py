from my_matrix import MyMatrix,\
                          SingularMatrixException

def main():
    try:
        array1 = [ [ 1.0, -1.0 ], \
                    [ 1.0,  1.0 ] ]
        matrixa = MyMatrix(array1)
        matrixa.display()
        matrixb = matrixa.inverse()
        matrixb.display()
        
        array2 = [ [ 1.0, -1.0 ], \
                    [ 1.0, -1.0 ] ]
        matrixa = MyMatrix(array2)
        matrixa.display()
        matrixb = matrixa.inverse()
        matrixb.display()
    except SingularMatrixException as sme:
        print('逆行列を計算できません。')
        
        
if __name__ == '__main__':
    main()
