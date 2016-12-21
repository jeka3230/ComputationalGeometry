from itertools import izip
from math import sqrt

def dot_product(v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

def norm_l2(v):
    return sqrt(dot_product(v, v))

def substraction(v1, v2):
    return tuple(x - y for x, y in zip(v1, v2))

def cosine(v1, v2):
    try:
        return dot_product(v1, v2) / norm_l2(v1) / norm_l2(v2)
    except:
        return 0

def vector_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]