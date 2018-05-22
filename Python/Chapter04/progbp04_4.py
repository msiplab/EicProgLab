import sys

def main(args):
    try:
        op1 = args[1]
        op2 = args[2]
        print('{0} + {1} = '.format(op1,op2), end='', flush=True)
        ans = sum(op1, op2)
        print('{0}'.format(ans))
    except ValueError:
        print('数値ではありません！', file=sys.stderr)


def sum(a,b):
    try:
        c = float(a) + float(b)
        return c
    except ValueError:
        raise

if __name__ == '__main__':
    main(sys.argv)
