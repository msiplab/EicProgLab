class MyStringStack:
    
    def __init__(self,stacksize):
        self.__mystack = \
            [ '' for idx in range(stacksize) ]
        """a"""
        self.__top = -1
        
        
    def pushdown(self,data):
        self.__top += 1
        """b"""
        self.__mystack[self.__top] = data
        
        
    def popup(self):
        """c"""
        self.__top -= 1
        return self.__mystack[self.__top+1]
        
    @property
    def top(self):
        """d"""
        return self.__top
