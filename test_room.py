from room import Position, RectangularRoom
import unittest, math

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        print('SetUp')
        # coordinates for valid position in room
        self.a = 1.0
        self.b = 1.0
        # Valid dimensions for room
        self.h = 10
        self.w = 10
        # Coordinates for (invalid) position outside room
        self.c = self.w + 1.0
        self.d = self.h + 1.0
        
        # Input to test exceptions
        # Input wrong type
        self.a1 = 'Three'
        # Input negative coordinates
        self.a2 = -1.0
        
        # Test instances
        self.room1 = RectangularRoom(self.w, self.h)
        self.position1 = Position(self.a, self.b)
        self.position2 = Position(self.c, self.d)

    def tearDown(self):
        pass
    
    def testInputForPosition(self):
        self.assertRaises(TypeError,Position,self.a1,self.b)
        self.assertRaises(TypeError,self.position1.getNewPosition,self.a1,self.a2)

    def testInputForRoom(self):
        expectedErr = [TypeError,ValueError,TypeError,AssertionError,AssertionError]
        fncs = [RectangularRoom,
                RectangularRoom,
                self.room1.cleanTileAtPosition,
                self.room1.isTileCleaned,
                self.room1.isPositionInRoom]
        inputs = [(self.a,self.b),
                (self.h,int(self.a2)),
                (self.a1,self.b),
                (self.a,self.b),
                (self.b,)]
        
        for example in range(len(expectedErr)):
            self.assertRaises(expectedErr[example],fncs[example],*inputs[example])
        
    def test_getX(self):
        self.assertEqual(self.position1.getX(),self.a)
    
    def test_getY(self):
        self.assertEqual(self.position1.getY(),self.b)

    def test_getNewPosition(self):
        ANGLE = 20
        SPEED = 10.0
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
        # Tiles not yet cleaned
        dx = 2
        dy = 3
        
        self.room1.cleanTileAtPosition(self.position1)
        self.assertTrue(self.room1.isTileCleaned(int(self.a), int(self.b)))
        self.assertFalse(self.room1.isTileCleaned(dx, dy))
    
    def test_getNumTiles(self):
        self.assertEqual(self.room1.getNumTiles(), self.w * self.h)
    
    def test_getNumCleanedTiles(self):
        clean_tiles = 0
        self.assertEqual(self.room1.getNumCleanedTiles(),clean_tiles)

    def test_getRandomPosition(self):
        room2 = RectangularRoom(self.w,self.h)
        new_randPos = room2.getRandomPosition()
        self.assertIsInstance(new_randPos,Position) 
        self.assertTrue(room2.isPositionInRoom(new_randPos))

    def test_isPositionInRoom(self):
        self.assertTrue(self.room1.isPositionInRoom(self.position1))
        self.assertFalse(self.room1.isPositionInRoom(self.position2))
