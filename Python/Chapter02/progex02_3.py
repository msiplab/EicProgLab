def main():
    
    x = [ 1.0, 3.0 ]                   # vector x
    a = [ [  .5, .5 ],                 # matrix A 
          [ -.5, .5 ] ]
    y = [ 0.0 for iRow in range(2) ]  # vector y
    
    for irow in range(len(y)):     # y = Ax
        for icol in range(len(x)):
            y[irow] += a[irow][icol] * x[icol]
    
    for irow in range(len(y)):
        print(y[irow])               # display y

if __name__  == '__main__':
    
    main()
