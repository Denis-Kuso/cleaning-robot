# Testing class Robot     
import unittest
from robot import *
from room import *

class TestRobot(unittest.TestCase):
    def SetUp(self):
        pass
    # Which functions take input
        # Robot instances: room:RecRoom, speed: float (>0)
        # Robot.setRobotPosition: position: Position
        # setRobotDirection: direction: angle in degrees (float )
         
a = 5
b = 10
speed = 1
room1 = RectangularRoom(a,b)
robot1 = Robot(room1,speed)
print(robot1.room.getNumTiles() == a*b)
print(robot1.room.getNumCleanedTiles() == 0)  
robot1.updatePositionAndClean()
print(robot1.room.getNumCleanedTiles() == 1)
robot1.updatePositionAndClean()
print(robot1.room.getNumCleanedTiles()==2)
# Check whether tTiles on which robot was located are clean
m = int(robot1.getRobotPosition().getX())
n = int(robot1.getRobotPosition().getY())
print(robot1.room.isTileCleaned(m,n)== False)
# After moving on to next tile, the previous tile should be clean
robot1.updatePositionAndClean()
print(robot1.room.isTileCleaned(m,n))
# TODO - all of my coordinates are floats, however my isTile cleaned is of type int, therefore I always get false
# should I convert to int the appending of coordinates in the  method cleanTileAtPosition
# Resolved this issue of returning false on isTileCleaned by converting to int the retriveal of position

# # # # Test standardRobot
# # initialise standard robot
# speed = 1
# robot_s = StandardRobot(room1, speed)
# robot_s.setRobotPosition(Position(1,1))
# for i in range(10):
#                 print('Iteration of for loop=',i)
#                 print(f' Current x pos = {robot_s.getRobotPosition().getX()}')
#                 print(f' Current y pos = {robot_s.getRobotPosition().getY()}')
                
#                 print('Updating position...')
#                 robot_s.updatePositionAndClean()
#                 # print('Tile is clean =',robot_s.room.isTileCleaned(int(self.getRobotPosition().getX()),int(self.getRobotPosition().getX())))
#                 # print('Updated position x =')
#                 # print('Updated position y =')
#                 print('\n')

# === Testing
# Instatiate robot and room
# room_rand = RectangularRoom(5,4)
# Robot_rand = RandomWalkRobot(room_rand,1)
# Robot_rand.updatePositionAndClean()
# # # visualize Random robot
# # runSimulation(1,1,10,10,0.90,1,RandomWalkRobot,True)
# n_of_ticks = []
# for room, fraction in zip(room_size,fractions):
#     # calculate mean time for different room size and different fraction (added as tuple)
#     n_of_ticks.append((runSimulation(num_robots,speed,room,room,fraction/100,30, RandomWalkRobot),(room,fraction)))
# for time in range(len(n_of_ticks)):
#     print(f'Room size {n_of_ticks[time][1][0]} * {n_of_ticks[time][1][0]} takes {round(n_of_ticks[time][0],0)} ticks to clean {n_of_ticks[time][1][1]}%')
# === Testing finished