import matplotlib.pyplot as plt
from Data import Data
from minPosition import minPosition
import os

def readData(path):
    inputFile = open(path, "r")
    data = map(float, inputFile.read().split())
    inputFile.close()
    return data

def writeValues(path, f):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, "w") as outputFile:
        print >> outputFile, len(f)
        print >> outputFile, " ".join(f)

def getCoordinates(data):
    pointsN = int(data[0])
    minSearch = minPosition()
    coordinates = []

    for i in xrange(pointsN):
        x = data[2 * i + 1]
        y = data[2 * i + 2]
        coordinates.append((x, y))
        minSearch.update(x, y, i)

    return Data(coordinates, minSearch.min_pos, pointsN)



def plot(F, savefig=None, show=None):
    maxF = max(F)
    plt.bar(range(len(F)), F)
    plt.title("F(m)")
    plt.xlabel("m")
    plt.ylabel("F")
    if maxF > 100:
        for a, b in zip(range(len(F)), F):
            plt.text(a + 0.2, int(b) + 1, str(b))
    if savefig:
        if not os.path.exists(os.path.dirname(savefig)):
            os.makedirs(os.path.dirname(savefig))
        plt.savefig(savefig)
    if show:
        plt.show()