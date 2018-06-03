import sys
from tv_factory import TvFactory
from tv_exception import TvException

def main(args):
    tvSpec = args[1]
    region = args[2]
    channel = int(args[3])
    
    try:
        tv = TvFactory.createtv(tvSpec)
        tv.region = region
        tv.display(channel)
    except TvException as te:
        print(te)
        
if __name__ == '__main__':
    main(sys.argv)
