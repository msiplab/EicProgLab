import math
from vector import Vector
class NormedVector(Vector):
    def __init__(self,array):
        super().__init__(array)

    def inner_product(self,another):
        result = 0.0
        for idx in range(len(self._array)):
            result += self._array[idx] * another._array[idx]
        return result

    def norm(self):
        return math.sqrt(self.inner_product(self))
