from person import Person
from cd import Cd
from cd_player import CdPlayer

def main():
	# Person をインスタンス化 
	taro = Person('太郎', 'アニメ')
	hanako = Person('花子', 'アイドル')
	
	# Cd をインスタンス化
	animecd = Cd('アニメ')
	
	# CdPlayer をインスタンス化
	panasonyplayer = CdPlayer()
	
	# panasonyPlayer に animecd をセット
	panasonyplayer.cd = animecd
	
	# taro と hanako に Cd を聞かせる
	taro.listentomusic(panasonyplayer)
	hanako.listentomusic(panasonyplayer)
	
	# taro と hanako の気分は？
	print('太郎の気分： ' + taro.kibun)
	print('花子の気分： ' + hanako.kibun)
    
if __name__ == '__main__':	
	main()
