class MyPhasor:
	
	def __init__(self,amplitude,phase):
		""" a """
		self.__amplitude = amplitude
		self.__phase = phase
		
	@property
	def amplitude(self):
		""" b """
		return self.__amplitude
		
	@property
	def phase(self):
		""" c """
		return self.__phase
		
	def prodconj(self,another):
		result = MyPhasor( \
		self.__amplitude * another.__amplitude, \
		self.__phase - another.__phase)
		""" d """
		return result
		
if __name__ == '__main__':
	
	phasor_v = MyPhasor(5.0, 0.0)
	phasor_i = MyPhasor(0.2, 45.0)
	
	print('|V| = {:6.2f}'.format(phasor_v.amplitude))
	print('∠I  = {:6.2f}'.format(phasor_i.phase))
	
	phasor_p = phasor_v.prodconj(phasor_i)
	
	print('|P| = {:6.2f}'.format(phasor_p.amplitude))
	print('∠P  = {:6.2f}'.format(phasor_p.phase))
