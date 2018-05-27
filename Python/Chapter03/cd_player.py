from cd import Cd

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
