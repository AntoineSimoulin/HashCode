from .util import get_ride_length

class Ride:
    def __init__(self, id, a, b, x, y, s, f):
        self.id = id
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.done = False
        self.length = get_ride_length(a, b, x, y)
