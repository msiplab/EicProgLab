class Vector:
    def __init__(self,array):
        self._array = array

    def add_to(self,another):
        for idx in range(len(self._array)):
            self._array[idx] += another._array[idx]

    def scale_by(self,scale):
        for idx in range(len(self._array)):
            self._array[idx] *= scale

    @property
    def array(self):
        return self._array
