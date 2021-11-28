import matplotlib.pyplot as plt
import visualize as vs
from room import *
from robot import *


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize = False):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.
    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.
    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    
    times = []
    # Repeat simulation num_trials times
    for trial in range(num_trials):
        if visualize:
            anim = vs.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        total_time = 0.0
        robotCollection =[]
        # Create num_robots of robots
        for i in range(num_robots):
            robotCollection.append(robot_type(room,speed))
        if visualize:
            anim.update(room, robotCollection)
            
        # Clean until desired coverage achieved
        while (room.getNumCleanedTiles()/float(room.getNumTiles())) < min_coverage:
            # Update positions of all robots
            for robot in robotCollection:
                robot.updatePositionAndClean()
            total_time += 1.0
            if visualize:
                anim.update(room, robotCollection)
        times.append(total_time)
        if visualize:
            anim.done()
        
    
    return sum(times)/len(times)


def showPlot1(saveFig = False):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # calculate mean time for 1-10 robots
    mean_times = []
    NUM_TRIALS = 10
    WIDTH = HEIGHT = 20
    CLEAN_FRACTION = 80
    SPEED = 1.0
    robo_number = []
    NUM_OF_ROBOTS = 10

    # Simulate cleaning of room with 1 up to NUM_OF_ROBOTS
    for robot in range(1, NUM_OF_ROBOTS+1):
        robo_number.append(robot)
        mean_times.append(runSimulation(robot,SPEED, WIDTH, HEIGHT, CLEAN_FRACTION/100,NUM_TRIALS,StandardRobot))
    
    # Plot
    fig_size = (10,5)
    fig = plt.figure(figsize = fig_size)
    title = 'Time to clean fraction of room with varried number of robots'
    axarr = plt.subplot(1,1,1)
    plt.style.use('ggplot')

    plt.plot(robo_number,mean_times,'bo-.',lw=2)
    plt.ylabel(f'Mean time with {NUM_TRIALS} trials')
    plt.minorticks_off()
    plt.xlabel('Number of robots')
    plt.title(f"Time to clean {CLEAN_FRACTION}% of a {WIDTH}x{HEIGHT} room")
    return fig
    
    if saveFig:
        plt.savefig(title + '.png')
    

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    NUM_OF_ROBOTS = 2
    CLEAN_FRACTION = 80
    NUM_TRIALS = 50
    SPEED = 1.0
    
    # Defined room dimensions all of same surface area
    ROOM_DIMENSIONS = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    mean_times = []
    wToH_ratio = []

    # Simulate cleaning room with dimensions of room in room_dimension
    Wdth = 0
    Hght = 1
    for room in range(len(ROOM_DIMENSIONS)):
        wToH_ratio.append(ROOM_DIMENSIONS[room][Wdth]/ROOM_DIMENSIONS[room][Hght])
        mean_times.append(runSimulation(NUM_OF_ROBOTS,SPEED, ROOM_DIMENSIONS[room][Wdth],ROOM_DIMENSIONS[room][Hght],CLEAN_FRACTION/100,NUM_TRIALS,StandardRobot))
    
    # Plot
    fig_size = (10,5)
    fig = plt.figure(figsize = fig_size) 
    axarr = plt.subplot(1,1,1)

    plt.plot(wToH_ratio,mean_times,"bo")
    plt.ylabel('Mean time')
    plt.minorticks_off()
    plt.xlabel('Width/height', size = 6)
    plt.title(f"Time to clean {CLEAN_FRACTION}% of a room with different width/height ratio")
    return fig

def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    # Define parameters
    mean_times_stand = []
    mean_times_rand = []
    num_trials = 10
    WIDTH = HEIGHT = 20
    CLEAN_FRACTION = 80
    NUM_ROBOTS = 15
    SPEED = 1.0
    robot_number = []

    # Simulate cleaning rooms with both types of robots from 1 to NUM_ROBOTS of robots
    for robot in range(1,NUM_ROBOTS + 1):
        robot_number.append(robot)
        mean_times_stand.append(runSimulation(robot,SPEED, WIDTH, HEIGHT,CLEAN_FRACTION/100,num_trials,StandardRobot))
        mean_times_rand.append(runSimulation(robot,SPEED, WIDTH, HEIGHT,CLEAN_FRACTION/100,num_trials,RandomWalkRobot))

    # Plot mean times
    fig_size = (10,5)
    fig = plt.figure(figsize = fig_size) 
    axarr = plt.subplot(1,1,1)

    plt.plot(robot_number,mean_times_stand,'bo-.', label = 'Standard Robot' )
    plt.plot(robot_number, mean_times_rand,'ro-.', label = 'Random walk robot')
    plt.legend(loc = 'best')
    plt.ylabel(f'Mean time with {num_trials} trials')
    plt.minorticks_off()
    plt.xlabel('Number of robots')
    plt.title(f"Time to clean {CLEAN_FRACTION}% of a {WIDTH}x{HEIGHT} room")
    return fig


def showPlots():
    plot1 = showPlot1()
    plot2 = showPlot2()
    plot3 = showPlot3()
    plt.show()

showPlots()