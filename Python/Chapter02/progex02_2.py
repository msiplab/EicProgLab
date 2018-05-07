def main():
	
	a = [ [ 1.0 ],
          [ 1.0, 2.0],
          [ 1.0, 2.0, 3.0] ]
	
	for iRow in range(len(a)):
		
		for iCol in range(len(a[iRow])):
			
			print(a[iRow][iCol], ' ', end='')
			
		print()

if __name__ == '__main__':
	
	main()
