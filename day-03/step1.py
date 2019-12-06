import math, cmath
from collections import namedtuple
Point = namedtuple('Point', ('x', 'y'))

def pointToStr(pt):
    return f"{pt.x},{pt.y}" 

def segmentToStr(segment):
    return f"{pointToStr(segment[0])}:{pointToStr(segment[1])}"

def getCoordinates(origin, direction, distance):
    if (direction == "L"):
        return Point(origin.x - distance, origin.y)
    elif (direction == "U"):
        return Point(origin.x, origin.y + distance)
    elif (direction == "R"):
        return Point(origin.x + distance, origin.y)
    elif (direction == "D"):
        return Point(origin.x, origin.y - distance)
    else:
        print(f"Oh boy, wrong input: [{direction}]")
        quit()

def getDistanceBetweenPoints(start, end):
    return abs(end.x - start.x) + abs(end.y - start.y)

def segmentsIntersect(segment1, segment2):
    return (intersectsHorizontally(segment1, segment2) \
            and intersectsVertically(segment2, segment1)) \
        or (intersectsHorizontally(segment2, segment1) \
            and intersectsVertically(segment1, segment2))

def intersectsHorizontally(segment1, segment2):
    for point in segment1:
        minX = min(segment2[0].x, segment2[1].x)
        maxX = max(segment2[0].x, segment2[1].x)
        if (point.x >= minX and point.x <= maxX):
            return True
    return False

def intersectsVertically(segment1, segment2):
    for point in segment1:
        minY = min(segment2[0].y, segment2[1].y)
        maxY = max(segment2[0].y, segment2[1].y)
        if (point.y >= minY and point.y <= maxY):
            return True
    return False

def findIntersections(segment, linesList):
    intersectedSegments = []
    for line in linesList:
        for pointNumber in range(len(line) - 1):
            currentSegment = (line[pointNumber], line[pointNumber + 1])
            if (segmentsIntersect(currentSegment, segment)):
                intersectedSegments.append(currentSegment)
        pointNumber = pointNumber + 1
    return intersectedSegments

def getIntersection(segment1, segment2):
    intersection = Point(0, 0)
    if (segment1[0].x != segment1[1].x):
        return Point(segment2[0].x, segment1[0].y)
    else:
        return Point(segment1[0].x, segment2[0].y)

def getLinePoints(filename):
    linesList = []
    input = open(filename, "r")
    startingPoint = Point(0, 0)
    lineNumber = 0
    for line in input:
        coordinate = startingPoint
        pointsList = [startingPoint]
        for bearing in line.split(","):
            coordinate = getCoordinates(coordinate, bearing[0], int(bearing[1:]))
            pointsList.append(coordinate)
        linesList.append(pointsList)
        lineNumber = lineNumber + 1
    return linesList

def main():
    linesList = getLinePoints("input.txt")
    minDistance = math.inf
    lineNumber = 0
    startingPoint = Point(0, 0)
    for line in linesList:
        for pointNumber in range(len(line) - 1):
            segment = (line[pointNumber], line[pointNumber + 1])
            linesToCheck = linesList[lineNumber + 1 :]
            for intersectedLine in findIntersections(segment, linesToCheck):
                intersection = getIntersection(segment, intersectedLine)
                distance = getDistanceBetweenPoints(startingPoint, intersection)
                if (distance > 0 and distance < minDistance):
                    minDistance = distance
        lineNumber = lineNumber + 1
    print(minDistance)

main()
