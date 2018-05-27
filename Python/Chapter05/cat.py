class Cat:
    
    def __init__(self, name, favorite, weight):
        self.__name = name
        self.__favorite = favorite
        self.__weight = weight
    
    def feed(self, food):
        if self.__favorite == food:
            self.__weight += 1
            
    @property
    def name(self):
        return self.__name
    
    @property
    def weight(self):
        return self.__weight    
    
