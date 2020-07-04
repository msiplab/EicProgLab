"""ジェネレータのサンプル"""
def fibonacci(max):
    a, b = 0, 1
    for n in range(max):
        c = a
        a, b = b, a + b
        yield c

if __name__=='__main__':
    for n in fibonacci(10):
        print(n, end=' ')