class MyMatrix:
    
    def __init__(self,array):
        self.__array = array
    
    
    def display(self):
        for irow in range(2):
            print(' [ ',end='')
            for icol in range(2):
                print('{0:6.2f} '.format(\
                    self.__array[irow][icol]),\
                    end='')
            print(' ] ')
        print()
    
    
    def inverse(self):
        a, b = self.__array[0][0], self.__array[0][1]
        c, d = self.__array[1][0], self.__array[1][1]
        det = a*d - b*c
        if abs(det) < 1e-300:
            raise SingularMatrixException()
        else:
            invarr = [ [  d/det, -b/det ], \
                        [ -c/det,  a/det ] ]
            return MyMatrix(invarr)


class SingularMatrixException(Exception):
    
    def __init__(self):
        super().__init__(self)
