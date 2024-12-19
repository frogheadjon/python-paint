#Python Paint Alpha TESTER
#Author: Aiden Johnson

import unittest
import math
from graphics import *

#for some reason when I do "from PythonPaintAlpha import getDistance" or "from PythonPaintAlpha import ColorCircle" 
#it just runs my code for that and doesn't test.. 
#But when I look at ShapeParserTester that imports the stuff with no problem.. :( 
# So I ended up just copy and pasting the stuff I was testing in here. 

def getDistance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

class ColorCircle():
    #Color Circle instance variables 
    def __init__(self, color, outline, x, y,):
        self.radius = 20
        self.color = color 
        self.outline = outline
        self.x = x
        self.y = y

    #Only method tested is didClick
    def didClick(self, clickX, clickY):
        distance = getDistance(self.x, self.y, clickX, clickY)
        if distance <= self.radius:
            return True 
        else:
            return False 

#I have written three tests for the getDistance() function, one that tests it with int values, 
#One that tests it with float values, and finally one that takes NO difference in distance. AKA all coordinates are 
#the same, so distance should equal 0. 

#A LOT of this code was copied from ShapeParserTester and from the base case tester thing on slack
# and then reimplemented to work for my code because 
# I had trouble understanding how to make tests for functions at first.

class TestGetDistance(unittest.TestCase):
    def testGetDistanceInt(self):
        # Test with integer coordinates. I used a pyhtagorean triple to test. First point is at (0,0) and the seocnd is at (6,8) hopefully returning 10.0 
        x1,y1,x2,y2 = 0, 0, 6, 8
        expectedDistance = 10.0
        actual = getDistance(x1,y1,x2,y2)
        self.assertEqual(actual, expectedDistance)
    
    def testGetDistanceFloat(self):
        # Test with float coordinates. I used the same pythogorean triple but as floats now. so everything got knocked one point by .1
        x1,y1,x2,y2 = 0.1, 0.1, 6.1, 8.1
        expectedDistance = 10.0
        actual = getDistance(x1,y1,x2,y2)
        self.assertEqual(actual, expectedDistance)

    def testGetDistanceNothing(self):
        # Test with completely identical coordinates that are all at (0,0)
        x1, y1, x2, y2 = 0, 0, 0, 0
        expectedDistance = 0.0
        actual = getDistance(x1,y1,x2,y2)
        self.assertEqual(actual, expectedDistance)

#All three of my tests have passed for getDistance! Yay.

#Now, I will check Color Circle method didClick() ... 
class TestDidClick(unittest.TestCase):
    def testDidClickInCircle(self):
       #first I created a color circle at 
       colorCircle = ColorCircle("black", "black", 100, 100)
       #second I made an ideal clickPoint that would be wihtin the color circle's radius
       clickPoint = Point(110,110)
       #third I used the didClick() method and got a result (HOPEFULLY TRUE)
       actual = colorCircle.didClick(clickPoint.getX(), clickPoint.getY())
       #Finally I tested it with assert equal. 
       self.assertEqual(actual, True)
       #It works!

    def testDidClickOutCircle(self):
       #first I created a color circle at 
       colorCircle = ColorCircle("black", "black", 100, 100)
       #second I made an ideal clickPoint that would be wihtin the color circle's radius
       clickPoint = Point(800,500)
       #third I used the didClick() method and got a result (HOPEFULLY FALSE)
       actual = colorCircle.didClick(clickPoint.getX(), clickPoint.getY())
       #Finally I tested it with assert equal. 
       self.assertEqual(actual, False)
       #It works!

if __name__ == "__main__":
    unittest.main(verbosity=2)