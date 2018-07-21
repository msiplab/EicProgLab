from interface_animal import IAnimal
class Mouse(IAnimal):
    @property
    def name(self):
        return '鼠'
    @property
    def type(self):
        return '哺乳類'
