import sys
from IO import *
import argparse

SLASH = "/"
TXT = ".txt"
PNG = ".png"

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="file name without extension", default="4node")
parser.add_argument("-i", "--input_folder", help="path to folder to input files", default="data/input")
parser.add_argument("-o", "--output_folder", help="path to folder to output files", default="data/output")
parser.add_argument("--show_plot", help="show bar plot", action="store_true", default=False)
args = parser.parse_args()

name = args.name
INPUT_FOLDER = args.input_folder + SLASH
OUTPUT_FOLDER = args.output_folder + SLASH
INPUT_FILE = INPUT_FOLDER + name + TXT
OUTPUT_FILE = OUTPUT_FOLDER + name + TXT
OUTPUT_BAR = OUTPUT_FOLDER + name + PNG

inputArray = readData(INPUT_FILE)
coordinates = getCoordinates(inputArray)
convexSize = sys.maxint
F = []

while coordinates.size() > 3:
    coordinates.sort()
    convexSize = coordinates.deleteOuterConvexHull()
    F.append(convexSize)

remain = coordinates.size()

if remain > 0:
    F.append(remain)

plot(F, OUTPUT_BAR, show=args.show_plot)
writeValues(OUTPUT_FILE, map(str, F))