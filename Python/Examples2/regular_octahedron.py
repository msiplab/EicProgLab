from i3d_object import IThreeDimensionalObject
import math

class RegularOctahedron(IThreeDimensionalObject):
	
    def is_inside(self, x, y, z):
        if (math.fabs(x) + math.fabs(y) + math.fabs(z)) <= 1.0:
            return True
        else:
            return False
            
    @property
    def name(self):
        return '正八面体'  
    
    @property
    def analytical_solution(self):
        return 4.0/3.0
