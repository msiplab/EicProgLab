def main():
	
	x = [ 1.0, 3.0 ]                   # vector x
	A = [ [  .5, .5 ],                 # matrix A 
		  [ -.5, .5 ] ]
	y = [ 0 for iRow in range(2) ]  # vector y
	
	for iRow in range(len(y)):     # y = Ax
		
		for iCol in range(len(x)):
			
			y[iRow] += A[iRow][iCol] * x[iCol]
	
	for iRow in range(len(y)):
		
		print(y[iRow])               # display y

if __name__  == '__main__':
	
	main()
