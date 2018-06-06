import sys
from plasma_tv import PlasmaTv
from lcd_tv import LcdTv
from tv_exception import TvException

def main(args):
    tvspec = args[1]
    region = args[2]
    channel = int(args[3])
    
    try:
        if tvspec == 'プラズマ':
            tv = PlasmaTv()
        elif tvspec == '液晶':
            tv = LcdTv()
        else:
            raise TvException(tvspec + 'は利用不可．')
        tv.region = region
        tv.display(channel)
    except TvException as te:
        print(te)
        
if __name__ == '__main__':
    main(sys.argv)
