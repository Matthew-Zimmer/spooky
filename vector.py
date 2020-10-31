
class Vector:
    def __init__(self, *values):
        self.values = values
    def clone(self):
        pass
    def norm(self):
        pass
    def unit(self):
        pass
    def __add__(self, other):
        pass
    def __sub__(self, other):
        pass
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            v = self.clone()
            v *= other
            return v
        else:
            return self._vector_mul(other)
    def __div__(self, other):
        pass
    def __iadd__(self, other):
        pass
    def __isub__(self, other):
        pass
    def __imul__(self, other):
        return self._scalar_mul(other)
    def __idiv__(self, other):
        pass
    def _vector_mul(self, other):
        pass
    def _scalar_mul(self, other):
        pass