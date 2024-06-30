from i3d_object import IThreeDimensionalObject
import math

class Sphere(IThreeDimensionalObject):
    
    def is_inside(self, x, y, z):
        if (x**2 + y**2 + z**2) <= 1.0:
            return True
        else:
            return False
            
    @property
    def name(self):
        return '球'  
        
    @property    
    def analytical_solution(self):
        return math.pi*4.0/3.0
