import progex03_5 as pe35

def main():
	# Person をインスタンス化 
	taro = pe35.Person('太郎', 'アニメ')
	hanako = pe35.Person('花子', 'アイドル')
	
	# Cd をインスタンス化
	animecd = pe35.Cd('アニメ')
	
	# CdPlayer をインスタンス化
	panasonyplayer = pe35.CdPlayer()
	
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
