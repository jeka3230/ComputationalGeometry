# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
from math import sqrt
import os


DATA_FOLDER = "data/"
INPUT_FOLDER = DATA_FOLDER + "input/"
OUTPUT_FOLDER = DATA_FOLDER + "output/"

def readPoints(filepath):
    inputFile = open(filepath)
    data = inputFile.read().splitlines()[1:]
    inputFile.close()
    points = - np.array([map(float, point.split()) for point in data])
    return points

def dist(x, y):
    d = x - y
    return np.sqrt(d.dot(d))


def triangleArea(simpic):
    a = edges[tuple(sorted([simpic[0], simpic[1]]))]
    b = edges[tuple(sorted([simpic[2], simpic[1]]))]
    c = edges[tuple(sorted([simpic[2], simpic[0]]))]
    p = float(a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


for filename in os.listdir(INPUT_FOLDER):
    points = readPoints(INPUT_FOLDER + filename.decode("utf-8"))

    triungulations = Delaunay(points)

    indices, neighbours = triungulations.vertex_neighbor_vertices

    edges = dict()

    for key in range(len(points)):
        for neighbour in neighbours[indices[int(key)]:indices[int(key) + 1]]:

            edge = tuple(sorted([key, neighbour]))
            distance = dist(points[edge[0]], points[edge[1]])
            edges[edge] = distance

    threshold = np.percentile(edges.values(), q=99)
    edges_delete = set()
    for (key, length) in edges.iteritems():
        if length > threshold:
            edges_delete.add(key)

    simplices = list(triungulations.simplices.copy())
    delete_indexes = []
    total_area = 0
    edges_number = dict()
    for key, simpic in enumerate(simplices):
        exist = True
        for i in xrange(3):
            current_edge = tuple(sorted([simpic[i], simpic[(i + 1) % 3]]))
            if current_edge in edges_delete:
                delete_indexes.append(key)
                exist = False
        if exist:
            total_area += triangleArea(simpic)
            for i in xrange(3):
                current_edge = tuple(sorted([simpic[i], simpic[(i + 1) % 3]]))
                try:
                    edges_number[current_edge] += 1
                except:
                    edges_number[current_edge] = 1



    hull = [key for (key, value) in edges_number.iteritems() if value == 1]
    perimeter = sum([edges[edge] for edge in hull])

    delete_indexes.reverse()
    for index in delete_indexes:
        del simplices[index]


    plt.figure(figsize=(20, 10))
    plt.title("area = {}, perimeter = {}".format(total_area, perimeter))
    data = []
    for edge in hull:
        point = points[edge[0]]
        point2 = points[edge[1]]
        plt.plot([point[0], point2[0]], [point[1], point2[1]])

    plt.plot(points[:, 0], points[:, 1], 'o')
    plt.savefig(OUTPUT_FOLDER + filename[:-4] + ".png")
    plt.clf()
