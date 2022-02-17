# Testing class Robot     
import unittest
from robot import Robot
from room import RectangularRoom,Position

class TestRobot(unittest.TestCase):
    def setUp(self):
        # Define test values
        self.speed = 1.0
        self.width = 10
        self.height = 10
        self.angle = 45
        # Define instances
        self.room = RectangularRoom(self.width, self.height)
        self.robot = Robot(self.room, self.speed)
        
    def testGetRobotPosition(self):
        self.assertIsInstance(self.robot.getRobotPosition(), Position)

    def testGetRobotDirection(self):
        
        self.zero = 0
        self.assertIsInstance(self.robot.getRobotDirection(),int)
        self.assertGreaterEqual(self.robot.getRobotDirection(),self.zero)

    def testSetRobotPosition(self):
        self.not_positionType = 3
        self.assertRaises(
                        TypeError,
                        self.robot.setRobotPosition,
                        self.not_positionType)

    def testUpdatePositionAndClean(self):
        curr_position = self.robot.getRobotPosition()
        self.room.cleanTileAtPosition(curr_position)
        new_position = self.robot.getRobotPosition().getNewPosition(self.angle,self.speed)
        # Positions must differ
        self.assertNotEqual(curr_position,new_position)

         
