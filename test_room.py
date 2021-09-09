from room import *
import unittest

class TestRoom(unittest.TestCase):
    # Create instances of Position and Room objects 
    
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

    def tearDown(self):
        pass

    def test_getX(self):
        self.assertEqual(self.position1.getX(),self.a)
    
    def test_getY(self):
        self.assertEqual(self.position1.getY(),self.b)

    def test_getNewPosition(self):
        ANGLE = 20
        SPEED = 10
        # Old coordinates and change in coordinates
        old_x = self.position1.getX()
        old_y = self.position1.getY()
        delta_x = SPEED * math.sin(math.radians(ANGLE))
        delta_y = SPEED * math.cos(math.radians(ANGLE))
        
        position3 = self.position1.getNewPosition(ANGLE, SPEED)
        # Expected coordinates
        exp_x = delta_x + old_x
        exp_y = delta_y + old_y
        
        self.assertIsInstance(position3, Position)
        self.assertAlmostEqual(position3.getX(),exp_x)
        self.assertAlmostEqual(position3.getY(),exp_y)
        

    def test_get_width(self):
        self.assertEqual(self.room1.get_width(),self.w)

    def test_get_height(self):
        self.assertEqual(self.room1.get_height(),self.h)

    def test_cleanTileAtPosition(self):
        # Provide tiles (one clean, one not clean, invalid tile, invalid output)
        # dirty tile
        dx = 2
        dy = 3
        
        self.room1.cleanTileAtPosition(self.position1)
        self.assertTrue(self.room1.isTileCleaned(self.a, self.b))
        self.assertFalse(self.room1.isTileCleaned(dx, dy))
    
    def test_getNumTiles(self):
        self.assertEqual(self.room1.getNumTiles(), self.w * self.h)
    
    def test_getNumCleanedTiles(self):
        self.assertEqual(self.room1.getNumCleanedTiles(),0)

    def test_getRandomPosition(self):
        room2 = RectangularRoom(self.w,self.h)
        new_randPos = room2.getRandomPosition()
        self.assertIsInstance(new_randPos,Position) 
        self.assertTrue(room2.isPositionInRoom(new_randPos))

    def test_isPositionInRoom(self):
        self.assertTrue(self.room1.isPositionInRoom(self.position1))
        self.assertFalse(self.room1.isPositionInRoom(self.position2))
