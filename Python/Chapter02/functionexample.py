import sys

def main(args):
	
	a = int(args[1])
	b = int(args[2])
	
	print('a+b= ',mysum(a,b))

def mysum(a,b):
	
	return a+b

if __name__ == '__main__':
	
	main(sys.argv)
