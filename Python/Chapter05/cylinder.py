from i3d_object import IThreeDimensionalObject
import math

class Cylinder(IThreeDimensionalObject):
	
    def is_inside(self, x, y, z):
        if (x**2+y**2) <= 1.0 and z >= 0.0:
            return True
        else:
            return False
            
    @property
    def name(self):
        return '円柱'  
    
    @property
    def analytical_solution(self):
        return math.pi
