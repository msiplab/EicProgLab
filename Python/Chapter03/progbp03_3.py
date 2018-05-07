import progex03_5 as pg35

def main():
	# Person をインスタンス化 
	taro = pg35.Person('太郎', 'アニメ')
	hanako = pg35.Person('花子', 'アイドル')
	
	# Cd をインスタンス化
	animeCd = pg35.Cd('アニメ')
	
	# CdPlayer をインスタンス化
	panasonyPlayer = pg35.CdPlayer()
	
	# panasonyPlayer に animeCd をセット
	panasonyPlayer.cd = animeCd
	
	# taro と hanako に Cd を聞かせる
	taro.listenToMusic(panasonyPlayer)
	hanako.listenToMusic(panasonyPlayer)
	
	# taro と hanako の気分は？
	print('太郎の気分： ' + taro.kibun)
	print('花子の気分： ' + hanako.kibun)
    
if __name__ == '__main__':
	
	main()
