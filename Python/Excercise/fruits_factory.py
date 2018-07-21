from goya import Goya
from suika import Suika
from lemon import Lemon


class FruitsFactory:
    @classmethod
    def create(cls,name):
        if name == 'Goya':
            return Goya()
        elif name == 'Suika':
            return Suika()
        elif name == 'Lemon': # """d"""
            return Lemon()
        else:
            return None
