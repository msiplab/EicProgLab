"""イテレータのサンプル"""
class Fibonacchi:

    def __init__(self,max):
        self.a, self.b = 0, 1
        self.max = max
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        c = self.a
        if self.n < self.max:
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
        else:
            raise StopIteration
        return c

if __name__ == '__main__':
    for n in Fibonacci(10):
        print(n, end=' ')