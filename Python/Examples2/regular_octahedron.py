from i3d_object import IThreeDimensionalObject

class RegularOctahedron(IThreeDimensionalObject):
	
    def isinside(self, x, y, z):
        if (x + y + z) <= 1.0:
            return True
        else:
            return False
            
    @property
    def name(self):
        return '正八面体'  
    
    @property
    def analyticalsolution(self):
        return 4.0/3.0
