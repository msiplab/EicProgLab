from ipdf import IProbabilityDensityFunction
import random

class Beta(IProbabilityDensityFunction):
    
    def parameter_inquiry(self):
        print('ベータ分布のパラメータ(α,β)を入力してください')
        self.alpha = float(input('α: '))
        self.beta  = float(input('β: '))

    def draw_sample(self):
        return random.betavariate(self.alpha,self.beta)
                    
    @property
    def name(self):
        return 'ベータ分布'  
        
    @property    
    def analytical_expectation(self):
        return self.alpha/(self.alpha+self.beta)
