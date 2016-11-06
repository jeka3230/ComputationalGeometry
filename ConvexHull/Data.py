from linalg import *
from minPosition import minPosition

class Data():

    def __init__(self, data, minY_pos, pointsN):
        self.data = data
        self.min_pos = minY_pos
        self.pointsN = pointsN
        self.start_position = self.data[self.min_pos]

    def cosine(self, v1):
        return cosine(v1, self.start_position)

    def sort(self):
        self.data = sorted(self.data, key=self.cosine, reverse=True)

    def deleteOuterConvexHull(self):

        point_last = 1
        indexes_delete = [0, 1]
        minSearch = minPosition()

        for position in xrange(2, self.pointsN):
            point_observe = self.data[position]
            point_next = self.data[(position + 1) % self.pointsN]
            vector_first = substraction(point_observe, self.data[point_last])
            vector_second = substraction(point_next, point_observe)
            if cosine(vector_first, vector_second) <= 0:
                point_last = position
                indexes_delete.append(position)
            else:
                minSearch.update(point_observe[0], point_observe[1], position)

        convexPower = len(indexes_delete)
        indexes_delete.reverse()
        foundMin = minSearch.min_pos
        minDecrease = 0

        for index in indexes_delete:
            del self.data[index]
            if index < foundMin:
                minDecrease += 1

        foundMin -=minDecrease
        self.min_pos = foundMin
        self.pointsN -= convexPower

        return convexPower

    def size(self):
        return len(self.data)