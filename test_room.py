from room import *
import unittest

class TestRoom(unittest.TestCase):
    # Create instances of position objects with atributes that test correct output of functions
    # Same for room objects
    
    # test for invalid input to instances of Room, position, or where input is given?
    def setUp(self):
        print('SetUp')
        self.a = 1
        self.b = 1
        self.h = 10
        self.w = 10
        self.c = self.w + 1 # Coordinates for position outside room
        self.d = self.h + 1
        
        self.room1 = RectangularRoom(self.w, self.h)
        self.position1 = Position(self.a, self.b)
        self.position2 = Position(self.c, self.d)

    def test_getX(self):
        self.assertEquals(self.position1.getX(),self.a)
    
    def test_getY(self):
        self.assertEquals(self.position1.getY(),self.b)
    def test_get_width(self):
        self.assertEquals(self.room1.get_width(),self.w)

    def test_get_height(self):
        self.assertEquals(self.room1.get_height(),self.h)

    def test_cleanTileAtPosition(self):
        pass
        #self.room1.cleanTileAtPosition(self.position1)
        #self.assertTrue(self.room1.isTileCleaned())
    
    
    def test_getNumTiles(self):
        self.assertEquals(self.room1.getNumTiles(),self.w * self.h)

    def test_isPositionInRoom(self):
        pass
# def test1():
#     yes = "Passed"
#     no = 'Failed'
#     # Instatiate Position object
#     a = 1
#     b = 1
#     position1 = Position(a,b)
#     # test retrevial of atributes
#     print('Testing retriveal of atrributes from Position object')
#     try:
#         assert position1.getX()== a 
#         assert position1.getY()== b
#         print(yes)
#     except AssertionError:
#         print(no)
#     print('\n')
#     ## Instatiate Rectangular room object
#     w = 10
#     h = 10
#     room1 = RectangularRoom(w,h)
#     ## test retrievial of atributes
#     print('Testing retrievial of atrributes from room object')
#     try:
#         assert room1.get_width()== w 
#         assert room1.get_height()== h
#         print(yes)
#     except AssertionError:
#         print(no)
#     print('\n')
#     ## Test cleaning of tiles
#     print('Testing cleaning of tiles')
#     room1.cleanTileAtPosition(position1)
#     try:
#         assert room1.isTileCleaned(a,b) == True
#         assert room1.isTileCleaned(2,3)== False
#         print(yes)
#     except AssertionError:
#         print(no)
    
#     print('\n')
#     print('Testing number of tiles')
#     try:
#         assert room1.getNumTiles() == w*h
#         position2 = room1.getRandomPosition()
#         print(yes)
#     except AssertionError:
#         print(no)
#     ## Is position inside the room
#     print('\n')
#     print("Testing position in room")
#     try:
#         assert room1.isPositionInRoom(position1) == True
#         print(yes)
#     except AssertionError:
#         print(no)
#     ## Create position outside room
#     position3 = Position(w + 2, h + 1)
#     try:
#         # position 3 should return False, since it is outside the room
#         assert room1.isPositionInRoom(position3) == False
#         print(yes)
#     except AssertionError:
#         print(no)
#test1()