from volume_calculator_exception import VolumeCalculatorException
from sphere import Sphere
from cylinder import Cylinder
from cone import Cone

class ThreeDimensionalObjectFactory:

    obj_list = [ 
                Sphere(), 
                Cylinder(),
                Cone()
                ]
            
    @classmethod
    def get_menu(cls): 
        menu = ''
        for idx in range(len(cls.obj_list)):
            menu += '{0}.\t {1}\n'.format(idx+1,cls.obj_list[idx].name)        
        return menu
        
        
    @classmethod
    def create(cls,name):
        if name == '1' or name == Sphere().name:
            return Sphere()
        elif name == '2' or name == Cylinder().name:
            return Cylinder()
        elif name == '3' or name == Cone().name:
            return Cone()            
        else:
            raise VolumeCalculatorException(name  + ' は無効です．')
        
