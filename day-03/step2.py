import math
from collections import namedtuple
Point = namedtuple('Point', ('x', 'y'))
 
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
            currentSegment = (line[pointNumber][0], line[pointNumber + 1][0])
            currentDistance = line[pointNumber][1]
            if (segmentsIntersect(currentSegment, segment)):
                intersectedSegments.append((currentDistance, currentSegment))
        pointNumber = pointNumber + 1
    return intersectedSegments

def getIntersection(segment1, segment2):
    if (isVertical(segment1)):
        return Point(segment1[0].x, segment2[0].y)
    else:
        return Point(segment2[0].x, segment1[0].y)

def getLinePoints(filename):
    linesList = []
    input = open(filename, "r")
    startingPoint = Point(0, 0)
    lineNumber = 0
    for line in input:
        coordinate = startingPoint
        totalDistance = 0
        pointsList = [(startingPoint, totalDistance)]
        for bearing in line.split(","):
            distance = int(bearing[1:])
            coordinate = getCoordinates(coordinate, bearing[0], distance)
            totalDistance = distance + totalDistance
            pointsList.append((coordinate, totalDistance))
        linesList.append(pointsList)
        lineNumber = lineNumber + 1
    return linesList

def isVertical(segment):
    return segment[0].x == segment[1].x

def main():
    linesList = getLinePoints("input.txt")
    minDistance = math.inf
    lineNumber = 0
    startingPoint = Point(0, 0)
    for line in linesList:
        for pointNumber in range(len(line) - 1):
            segment1 = (line[pointNumber][0], line[pointNumber + 1][0])
            distSegment1 = line[pointNumber][1]
            for intersections in findIntersections(segment1, linesList[lineNumber + 1 :]):
                distSegment2, segment2 = intersections
                intersection = getIntersection(segment1, segment2)
                if (isVertical(segment1)):
                    distIntersectionX = abs(intersection.x - segment2[0].x)
                    distIntersectionY = abs(intersection.y - segment1[0].y)
                else:
                    distIntersectionX = abs(intersection.x - segment1[0].x)
                    distIntersectionY = abs(intersection.y - segment2[0].y)
                distance = distSegment1 + distSegment2 + distIntersectionX + distIntersectionY
                if (segment1[0] != startingPoint and segment2[0] != startingPoint and distance < minDistance):
                    minDistance = distance
        lineNumber = lineNumber + 1
    print(minDistance)

main()
