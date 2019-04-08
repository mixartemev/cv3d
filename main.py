import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%d,%d)" % (self.x, self.y)


class Line:
    def __init__(self, tg: float, x0: float = 0, y0: float = 0):
        self.tg = tg
        self.x0 = x0
        self.y0 = y0

    def __repr__(self):
        return "y=%f*(x-%d)+%d" % (self.tg, self.x0, self.y0)


class Cam:
    def __init__(self, coord: Point, angle: float, angle_wide: float):
        self.coord = coord
        self.angle = angle
        self.angleWide = angle_wide

    def get_line(self, matrix: list, target: float) -> Line:
        ml = matrix.__len__()-1  # -1 its for ideal points
        idx = matrix.index(target)
        rel_idx = idx - ml/2
        angle_ratio = self.angleWide / ml
        rel_angle = rel_idx * angle_ratio
        target_angle = self.angle - rel_angle  # minus because counter clockwise
        tg = math.tan(math.radians(target_angle))
        return Line(tg, self.coord.x, self.coord.y)


p1 = Point(0, 0)
p2 = Point(7, 0)
c1 = Cam(p1, 45, 53)
c2 = Cam(p2, 90, 80.4)
m1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
m2 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l1 = c1.get_line(m1, 1)
l2 = c2.get_line(m2, 1)

print(l1, l2)
