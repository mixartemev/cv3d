import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    def __init__(self, tg: float, x0: float = 0, y0: float = 0):
        self.tg = tg
        self.x0 = x0
        self.y0 = y0


class Cam:
    def __init__(self, coord: Point, angle: float, angle_wide: int):
        self.coord = coord
        self.angle = angle
        self.angleWide = angle_wide

    def get_line(self, matrix: list, target: float) -> Line:
        ml = matrix.__len__()
        idx = matrix.index(target)
        rel_idx = idx - ml/2
        rel_angle = rel_idx * self.angleWide / ml
        target_angle = self.angle + rel_angle
        tg = math.tan(math.radians(target_angle))
        return Line(tg, self.coord.x, self.coord.y)
