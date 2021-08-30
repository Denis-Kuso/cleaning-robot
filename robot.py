#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:38:25 2021
@author: deniskusic
"""
# Problem Set 6: Simulating robots
# Name: Denis
# Collaborators: Tamara pomalo
# Time:

import math
import random as random
from room import Position
import visualize


class Robot(object):
    """
    Represents a robot cleaning a particular room.
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        # Choose x and y coordinates within the room
        self.position = self.room.getRandomPosition()
        #self.position = Position(random.choice(range(room.get_width())),random.choice(range(room.get_height())))
        self.direction = random.choice(range(360))
        # Should I clean the tile here?

    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        self.position = Position(position.getX(),position.getY())

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Clean tile at current position
        self.room.cleanTileAtPosition(self.getRobotPosition())
        # Change position, looks cluttered
        self.setRobotPosition(self.getRobotPosition().getNewPosition(self.direction,self.speed))


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.
    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Clean tile at current position
        self.room.cleanTileAtPosition(self.getRobotPosition())
        
        # Try changing position
        potential_pos = self.getRobotPosition().getNewPosition(self.direction,self.speed)
        # Change potential positions so the wall is not hit 
        while self.room.isPositionInRoom(potential_pos)==False:
            # # Change direction randomly and update possible position
            #print('entered while loop')
            self.direction = random.choice(range(360))
            #print('Trying new direction =', self.direction)
            potential_pos = self.getRobotPosition().getNewPosition(self.direction,self.speed)
        
        # Move robot
        self.setRobotPosition(potential_pos)
        


# === Problem 4
#
# 1) How long does it take to clean 80% of a 20◊20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions 
#	 20◊20, 25◊16, 40◊10, 50◊8, 80◊5, and 100◊4?

# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # Clean tile at current position
        self.room.cleanTileAtPosition(self.getRobotPosition())
        
        # Try changing position
        potential_pos = self.getRobotPosition().getNewPosition(random.randint(0,359),self.speed)
        # Change potential position if the wall would be hit 
        while self.room.isPositionInRoom(potential_pos)==False:
            # # Change direction randomly and update possible position
            self.direction = random.choice(range(360))
            potential_pos = self.getRobotPosition().getNewPosition(random.randint(0,359),self.speed)
        
        # Move robot
        self.setRobotPosition(potential_pos)

    
# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
