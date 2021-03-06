import random
import math


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        if type(x) != float or type(y) != float:
            print('Position accepts coordinates of type: float')
            raise TypeError
        else:
            self.x = x
            self.y = y

    def __repr__(self):
        return f'Position({self.x}, {self.y})'
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.
        Does NOT test whether the returned position fits inside the room.
        angle: int representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed
        Returns: a Position object representing the new position.
        """
        if type(angle) != int or type(speed) != float:
            raise TypeError
        elif angle > 360 or angle < 0 or speed <0:
            raise ValueError
        else:
            old_x, old_y = self.getX(), self.getY()
            # Compute the change in position
            delta_y = speed * math.cos(math.radians(angle))
            delta_x = speed * math.sin(math.radians(angle))
            # Add that to the existing position
            new_x = old_x + delta_x
            new_y = old_y + delta_y
            return Position(new_x, new_y)


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.
    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        width: an integer > 0
        height: an integer > 0
        """
        if type(width) != int or type(height) != int:
            raise TypeError
        elif width<=0 or height <=0:
            print('Room can only have dimensions greater than zero')
            raise ValueError
        
        else:
            self.width = width
            self.height = height
            self.cleaned_tiles = []

    def __repr__(self):
        return f'RectangularRoom({self.width} , {self.height})'

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.
        pos: a Position
        """
        if not isinstance(pos,Position):
            print('Position needs to be of type: Position')
            raise TypeError
        else:    
            # add current location to cleaned tiles
            if (int(pos.getX()),int(pos.getY())) not in self.cleaned_tiles:
                self.cleaned_tiles.append((int(pos.getX()),int(pos.getY())))
    

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.
        Assumes that (m, n) represents a valid tile inside the room.
        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        assert (type(m) and type(n)) == int
        if (m,n) in self.cleaned_tiles:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.
        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.
        returns: an integer
        """
        
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.
        returns: a Position object.
        """
        # Initialise variables for tiles
        x_s = []
        y_s = []
        x = 0
        y = 0
        coords = []
        
        # Generate tiles for the entire room  
        for x,y in zip(range(self.get_width()),range(self.get_height())):
            x_s.append(x)
            y_s.append(y)
            coords.append((x,y))
            x += 1
            y += 1
        
        # Choose randomly from all the tiles in room
        rand_x = random.choice(x_s)
        rand_y = random.choice(y_s)
        
        return Position(float(rand_x),float(rand_y))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        assert isinstance(pos, Position)
        if (0 <= pos.getX() <= self.get_width()) and (0 <= pos.getY() <= self.get_height()):
            return True
        else:
            return False
