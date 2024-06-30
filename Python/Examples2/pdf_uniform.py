from ipdf import IProbabilityDensityFunction
import random

class Uniform(IProbabilityDensityFunction):

    def parameter_inquiry(self):
        print('一様分布の範囲[a,b]を入力してください')
        self.__a = float(input(' a: '))
        self.__b = float(input(' b: '))

    def draw_sample(self):
        return random.uniform(self.__a,self.__b)
            
    @property
    def name(self):
        return '一様分布'  
        
    @property    
    def analytical_expectation(self):
        return (self.__a+self.__b)/2.0
