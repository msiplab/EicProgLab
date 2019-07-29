def main():
	
	try:
		for id in range(1,5):
			hand = RockPaperScissors.pon(id)
			print(str(id) + ': ' + hand)
			
	except RockPaperScissorsException as rpse:
		print(rpse)

class RockPaperScissors:
	
	@classmethod
	def pon(cls,id):
			
		ROCK = 1
		PAPER = 2
		SCISSORS = 3
	
		if id == ROCK:
			return 'グー'
		elif id == PAPER:
			return 'パー'
		elif id == SCISSORS:
			return 'チョキ'
		else:
			msg = 'その手はありません．'
			raise RockPaperScissorsException(msg)

class RockPaperScissorsException(Exception):
	
	def __init__(self, msg):
		super().__init__(msg)

if __name__ == '__main__':
	main()
