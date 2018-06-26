from volume_calculator_exception import VolumeCalculatorException
from sphere import Sphere
from regular_octahedron import RegularOctahedron

class ThreeDimensionalObjectFactory:

    objlist = [ 
                Sphere(), 
                RegularOctahedron()
                ]
            
    @classmethod
    def getMenu(cls): 
        menu = ''
        for idx in range(len(cls.objlist)):
            menu += '{0}.\t {1}\n'.format(idx+1,cls.objlist[idx].name)        
        return  menu
        
        
    @classmethod
    def create(cls,name):
        if name == '1' or name == Sphere().name:
            return Sphere()
        elif name == '2' or name == RegularOctahedron().name:
            return RegularOctahedron()
        else:
            raise VolumeCalculatorException(name  + ' は無効です．')
        
