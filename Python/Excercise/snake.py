from interface_animal import IAnimal
class Snake(IAnimal):
    @property
    def name(self):
        return '蛇'
    @property
    def type(self):
        return '爬虫類'
