from room import *

def test1():
    yes = "Passed"
    no = 'Failed'
    # Instatiate Position object
    a = 1
    b = 1
    position1 = Position(a,b)
    # test retrevial of atributes
    print('Testing retriveal of atrributes from Position object')
    try:
        assert position1.getX()== a 
        assert position1.getY()== b
        print(yes)
    except AssertionError:
        print(no)
    print('\n')
    ## Instatiate Rectangular room object
    w = 10
    h = 10
    room1 = RectangularRoom(w,h)
    ## test retrievial of atributes
    print('Testing retrievial of atrributes from room object')
    try:
        assert room1.get_width()== w 
        assert room1.get_height()== h
        print(yes)
    except AssertionError:
        print(no)
    print('\n')
    ## Test cleaning of tiles
    print('Testing cleaning of tiles')
    room1.cleanTileAtPosition(position1)
    try:
        assert room1.isTileCleaned(a,b) == True
        assert room1.isTileCleaned(2,3)== False
        print(yes)
    except AssertionError:
        print(no)
    
    print('\n')
    print('Testing number of tiles')
    try:
        assert room1.getNumTiles() == w*h
        position2 = room1.getRandomPosition()
        print(yes)
    except AssertionError:
        print(no)
    ## Is position inside the room
    print('\n')
    print("Testing position in room")
    try:
        assert room1.isPositionInRoom(position1) == True
        print(yes)
    except AssertionError:
        print(no)
    ## Create position outside room
    position3 = Position(w + 2, h + 1)
    try:
        # position 3 should return False, since it is outside the room
        assert room1.isPositionInRoom(position3) == False
        print(yes)
    except AssertionError:
        print(no)
test1()