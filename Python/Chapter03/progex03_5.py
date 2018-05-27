from person import Person

def main():
	
	taro = Person('太郎','アニメ')
	hanako = Person('花子','アイドル')
	
	print('太郎の気分：' + taro.kibun)
	print('花子の気分：' + hanako.kibun)

if __name__ == '__main__':
	main()

