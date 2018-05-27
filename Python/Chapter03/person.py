class Person:
	def __init__(self, name, konomi):
		self.__name = name
		self.__konomi = konomi
		self.kibun = '普通'
		
	def listentomusic(self, cdplayer):
		genre = cdplayer.playCd()
		if genre == self.__konomi:
			self.kibun = '楽しい' # ジャンル=好み
		else:
			self.kibun = 'イライラ' # ジャンル≠好み
