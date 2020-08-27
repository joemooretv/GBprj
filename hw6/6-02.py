class Road:
    _length: int
    _width: int

    def __init__(self, _length_m, _width_m):
        self._length = _length_m
        self._width = _width_m

    def asphalt_mass(self, mass_cm_sq_m, depth_cm):
        return self._length * self._width * mass_cm_sq_m * depth_cm


a = Road(20, 5000)
print(a.asphalt_mass(25, 5))
