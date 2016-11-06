import sys

class minPosition():

    def __init__(self):
        self.minX, self.minY = sys.float_info.max, sys.float_info.max
        self.min_pos = -1

    def update(self, x, y, i):
        if y < self.minY:
            self.minY, self.minX = x, y
            self.min_pos = i
        elif y == self.minY and x < self.minX:
            self.minY, self.minX = x, y
            self.min_pos = i