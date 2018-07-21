from interface_animal import IAnimal
class Dragon(IAnimal):
    @property
    def name(self):
        return '龍'
    @property
    def type(self):
        return '霊獣'
