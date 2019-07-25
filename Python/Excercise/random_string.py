import random

class RandomString:
    def __init__(self,itemlist):
        """b"""
        self.__itemlist = itemlist
        self.__nitems = len(self.__itemlist)

    def get_item_at(self,idx):
        """c"""
        return self.__itemlist[idx]

    def next(self):
        idx = random.randint(0,self.__nitems-1)
        """d"""
        return self.get_item_at(idx)
