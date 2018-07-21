from mouse import Mouse
from dragon import Dragon
from snake import Snake
class AnimalFactory:
    @classmethod
    def create(cls,name):
        if name == 'Mouse':
            return Mouse()
        elif name == 'Dragon':
            return Dragon()
        elif name == 'Snake':
            return Snake()
        else:
            return None
