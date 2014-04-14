# Amstelhaege Heuristieken 2014

import math
import random

BOTTOMLEFT, BOTTOMRIGHT = 0, 1
TOPLEFT, TOPRIGHT = 2, 3

def minDistance(buildingA, buildingB):
    positionA = buildingA.getPosition()
    positionB = buildingB.getPosition()
    minDist = 200
    xRangeA = (positionA[BOTTOMLEFT].getX(),
                        positionA[BOTTOMRIGHT].getX())
    yRangeA = (positionA[BOTTOMLEFT].getY(),
                        positionA[TOPLEFT].getY())
                        
    for i in [BOTTOMLEFT, BOTTOMRIGHT, TOPLEFT, TOPRIGHT]:
        if xRangeA[0] < positionB[i].getX() < xRangeA[1]:
            for j in [BOTTOMLEFT, BOTTOMRIGHT, TOPLEFT, TOPRIGHT]:
                dist = abs(positionB[i].getY() - positionA[j].getY())
                if dist < minDist:
                    minDist = dist
        elif yRangeA[0] < positionB[i].getY() < yRangeA[1]:
            for j in [BOTTOMLEFT, BOTTOMRIGHT, TOPLEFT, TOPRIGHT]:
                dist = abs(positionB[i].getX() - positionA[j].getX())
                if dist < minDist:
                    minDist = dist
        else:
            for j in [BOTTOMLEFT, BOTTOMRIGHT, TOPLEFT, TOPRIGHT]:
                distX = positionA[i].getX() - positionB[j].getX()
                distY = positionA[i].getY() - positionB[j].getY()
                dist = math.sqrt(distX**2+distY**2)
                if dist < minDist:
                    minDist = dist
    return minDist
        
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
 
# Area is a suboptimal name; choose different name.
class Area(object):
    def __init__(self, width=120, height=160):
        self.width = int(round(width))
        self.height = int(round(height))
    def getAreaWidth(self):
        return self.width
    def getAreaHeight(self):
        return self.height
    def startPos(self, minSpace, width, length):
        # Find out in what corner the origin of the visualization
        # is situated.
        #
        # Currently: assuming the origin is situated in the
        # bottom left corner.
        #
        # Confirmed, the bottom left corner is the origin of the
        # visualization.
        bottomLeftCorner = Position(minSpace, minSpace)
        bottomRightCorner = Position(minSpace + width, minSpace)
        topLeftCorner = Position(minSpace, minSpace + length)
        topRightCorner = Position(minSpace + width, minSpace + length)
        return [bottomLeftCorner, 
                bottomRightCorner,
                topLeftCorner,
                topRightCorner]
    def isPosInRoom(self, pos):
        x = pos.getX()
        y = pos.getY()
        if 0 <= x <= self.width and 0 <= y <= self.height:
            return True
        else:
            return False
            
class House(object):
    def __init__(self, width, length, value, valueIncrease, minSpace, area):
        self.width = width
        self.length = length
        self.value = value
        self.valueIncrease = valueIncrease
        self.minSpace = minSpace
        self.area = area
        self.position = area.startPos(minSpace, width, length)
    def getPosition(self):
        return self.position
    def rotateInit(self):
        self.position = area.startPos(minSpace, length, width)
    def rotateMiddle(self, point):
        posList = self.position
        xMiddle = (position[BOTTOMLEFT].getX() + positionA[BOTTOMRIGHT].getX())/2
        yMiddle = (position[BOTTOMLEFT].getY() + positionA[TOPLEFT].getY())/2
        middle = Position(xMiddle, yMiddle)
        self.position = [Position(xMiddle - length/2, yMiddle - width/2),
                         Position(xMiddle + length/2, yMiddle - width/2),
                         Position(xMiddle - length/2, yMiddle + width/2),
                         Position(xMiddle + length/2, yMiddle + width/2)]
        self.width = length
        self.length = width                              
    def move(self, direction, movedist):
        posList = self.position
        for point in posList:
            point[direction] = point[direction] - movedist

def overlap(buildingA, buildingB):
    positionA = buildingA.getPosition()
    positionB = buildingB.getPosition()
    xRangeA = (positionA[BOTTOMLEFT].getX(),
               positionA[BOTTOMRIGHT].getX())
    yRangeA = (positionA[BOTTOMLEFT].getY(),
               positionA[TOPLEFT].getY())
    for i in [BOTTOMLEFT, BOTTOMRIGHT, TOPLEFT, TOPRIGHT]:
      if xRangeA[0] <= positionB[i].getX() <= xRangeA[1] and yRangeA[0] <= positionB[i].getY() <= yRangeA[1]:
            return True
    else:
      return False

def testOverlap():
  region = Area()
  A = House(1, 2, 'value', 'valueincrease', 0, region)
  B = House(1, 2, 'value', 'valueincrease', 5, region)
  print overlap(A, B)
  
testOverlap()

def testMinDistance():
    region = Area()
    A = House(1, 2, 'value', 'valueincrease', 0, region)
    B = House(1, 2, 'value', 'valueincrease', 3, region)
    #print "House A position:", A.getPosition().getX(), A.getPosition().getY()
    print minDistance(A, B)

testMinDistance()

def setHouses():
    region = Area()
    numHouses = 5
    houseList = []
    for i in range(numHouses):
        newHouse = House(8, 8, 285, 0.03, 2, region)
        bottomLeftCorner = Position(random.randint(0, 120),
                                     random.randint(0,160))
        newHouse.position = [bottomLeftCorner,
                             Position(bottomLeftCorner.getX() + newHouse.width,
                                      bottomLeftCorner.getY()),
                             Position(bottomLeftCorner.getX(),
                                      bottomLeftCorner.getY() + newHouse.length),
                             Position(bottomLeftCorner.getX() + newHouse.width,
                                      bottomLeftCorner.getY() + newHouse.length)]
        houseList.append(newHouse)f
    return houseList

# Still missing:
# - Distance between houses;
# - Determination of the shortest distance + selection of associated nodes;
# - 3 different types of houses;
# - Calculation of region value.

