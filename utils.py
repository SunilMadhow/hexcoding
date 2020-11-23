from math import *
#approximately adapted from https://www.redblobgames.com/grids/hexagons/

class Hex:  # cube coordinates
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r


class Orientation:
    def __init__(self, forward, inverse, start_angle):
        self.forward = forward
        self.inverse = inverse
        self.start_angle = start_angle


flat = Orientation([sqrt(3.0), sqrt(3.0) / 2.0, 0.0, 3.0 / 2.0],
                   [sqrt(3.0) / 3.0, -1.0 / 3.0, 0.0, 2.0 / 3.0],
                   0.5)

pointy = Orientation([3.0 / 2.0, 0.0, sqrt(3.0) / 2.0, sqrt(3.0)],
                     [2.0 / 3.0, 0.0, -1.0 / 3.0, sqrt(3.0) / 3.0],
                     0.0)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Layout:
    def __init__(self, orientation : Orientation, size : Point, origin : Point):
        self.orientation = orientation
        self.size = size
        self.origin = origin

    def matrix_mul(self, vector: Point): #2x2
        x = self.orientation.forward[0] * vector.x + self.orientation.forward[1] * vector.y
        y = self.orientation.forward[2] * vector.x + self.orientation.forward[3] * vector.y
        return Point(x, y)

    @staticmethod
    def cube_round(p, q, r):
        p_, q_, r_ = round(p), round(q), round(r)
        pdelta, qdelta, rdelta = abs(p - p_), abs(q - q_), abs(r - r_)
        if pdelta > qdelta and pdelta > rdelta:
            p_ = -q_ - r_
        elif qdelta > rdelta:
            q_ = -p_ - r_
        else:
            r_ = -p_ - q_
        return Hex(p_, q_, r_)

    def euclidean_to_hex(self, point: Point) -> Hex: #a change of basis to calculate the cube-coordinates of a point in two dimensional euclidean space
        pt = Point(self.origin.x - point.x, self.origin.y - point.y)
        hex_points = self.matrix_mul(pt)
        return self.cube_round(hex_points.x, hex_points.y,  - hex_points.x - hex_points.y)