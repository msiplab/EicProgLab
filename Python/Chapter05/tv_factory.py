from plasma_tv import PlasmaTv
from lcd_tv import LcdTv
from crt_tv import CrtTv
from tv_exception import TvException

class TvFactory:
    
    @classmethod
    def createtv(cls, tvspec):
        if tvspec == 'プラズマ':
            return PlasmaTv()
        elif tvspec == '液晶':
            return LcdTv()
        else:
            raise TvException(tvspec + 'は利用不可．')
