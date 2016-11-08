from linalg import *
from minPosition import minPosition

def greater(x):
    if x > 0:
        return -1
    else:
        return 1

class Data():

    def __init__(self, data, min_pos, pointsN):
        self.data = data
        self.min_pos = min_pos
        self.pointsN = pointsN
        self.start_position = self.data[self.min_pos]

    def cosine(self, v):
        return cosine(substraction(v, self.start_position), (1, 0))

    def norm_l2(self, v):
        return norm_l2(substraction(v, self.start_position))

    def compare(self, x, y):
        sub_cos = self.cosine(x) - self.cosine(y)

        if sub_cos != 0:
            return greater(sub_cos)
        else:
            return greater(self.norm_l2(x) - self.norm_l2(y) < 0)

    def sort(self):
        del self.data[self.min_pos]
        self.data =[self.start_position] + sorted(self.data, cmp=self.compare)

    def deleteOuterConvexHull(self):

        indexes_delete = [0, 1]

        for position in xrange(2, self.pointsN):

            point_observe = self.data[position]

            while vector_product(substraction(self.data[indexes_delete[-1]], self.data[indexes_delete[-2]]), substraction(point_observe, self.data[indexes_delete[-1]])) < 0:
                indexes_delete.pop()
            indexes_delete.append(position)

        convexPower = len(indexes_delete)
        indexes_delete.reverse()

        for index in indexes_delete:
            del self.data[index]

        minSearch = minPosition()

        for i, element in enumerate(self.data):
            minSearch.update(element[0], element[1], i)

        self.min_pos = minSearch.min_pos
        self.start_position = minSearch.getPoint()
        self.pointsN -= convexPower

        return convexPower

    def size(self):
        return len(self.data)