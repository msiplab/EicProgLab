class Person:
	def __init__(self, name, konomi):
		self.__name = name
		self.__konomi = konomi
		self.kibun = '普通'
		
	def listentomusic(self, cdplayer):
		genre = cdplayer.playcd()
		if genre == self.__konomi:
			self.kibun = '楽しい' # ジャンル=好み
		else:
			self.kibun = 'イライラ' # ジャンル≠好み

class Cd:
	def __init__(self, genre):
		 self.__genre = genre
		 
	@property
	def genre(self):
		return self.__genre

class CdPlayer:

	@property
	def cd(self):
		pass # 何もしない
		
	@cd.setter
	def cd(self, cd):
		if isinstance(cd, Cd):
		    self.__cd = cd
	
	def playCd(self):
		return self.__cd.genre

if __name__ == '__main__':
	
	taro = Person('太郎','アニメ')
	hanako = Person('花子','アイドル')
	
	print('太郎の気分：' + taro.kibun)
	print('花子の気分：' + hanako.kibun)
