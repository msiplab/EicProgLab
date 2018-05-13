def main():
	
	a = [ [ 1.0 ],
          [ 1.0, 2.0],
          [ 1.0, 2.0, 3.0] ]
	
	for irow in range(len(a)):
		
		for icol in range(len(a[irow])):
			
			print(a[irow][icol], ' ', end='')
			
		print()

if __name__ == '__main__':
	
	main()
