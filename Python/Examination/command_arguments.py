import sys
def main(args):
    nargs = len(args)
    print('nargs = {0}'.format(nargs))
    for iarg in range(nargs):
        print('{0:d}: {1}'.format(iarg,args[iarg]))

if __name__ == '__main__':
    main(sys.argv)
