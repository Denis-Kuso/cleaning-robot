import matplotlib.pyplot as plt
import visualize 
from room import *
from robot import *
# # Run simulations for MIT's room sizes and fraction of room cleaned
# n_of_ticks = []
# for room, fraction in zip(room_size,fractions):
#     # calculate mean time for different room size and different fraction (added as tuple)
#     n_of_ticks.append((runSimulation(num_robots,speed,room,room,fraction/100,30, StandardRobot),(room,fraction)))
# for time in range(len(n_of_ticks)):
#     print(f'Room size {n_of_ticks[time][1][0]} * {n_of_ticks[time][1][0]} takes {round(n_of_ticks[time][0],0)} to clean {n_of_ticks[time][1][1]}%')
# ==== TESTING FINISHED

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
            anim = visualize.RobotVisualization(num_robots, width, height)
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

# ==== Testing vs MIT guidelines

# MIT's parameteres
# room_size =[5,10,10,20]# One dimension of the room, other is the same
# fractions = [100,75,90,100]# Percentage of room cleaned
# MIT_n_of_ticks = [150,190,310,3250]# Time taken for room to be cleaned for the desired fraction and size
# speed = 1.5
# num_robots = 1


def showPlot1(saveFig=False):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # calculate mean time for 1-10 robots
    mean_times = []
    num_trials = 10
    width = height = 20
    clean_fraction = 80
    robo_number = []
    NUM_OF_ROBOTS = 10

    # Simulate cleaning of room with 1 up to NUM_OF_ROBOTS
    for robot in range(1,NUM_OF_ROBOTS +1):
        robo_number.append(robot)
        mean_times.append(runSimulation(robot,1, width, height,clean_fraction/100,num_trials,StandardRobot))
    
    # Plot
    title = 'Time to clean fraction of room with varried number of robots'
    plt.style.use('ggplot')
    plt.plot(robo_number,mean_times,'bo-.',lw=2)
    plt.ylabel(f'Mean time with {num_trials} trials')
    plt.minorticks_off()
    plt.xlabel('Number of robots')
    plt.title(f"Time to clean {clean_fraction}% of a {width}x{height} room")
    plt.show()
    
    if saveFig:
        plt.savefig(title + '.png')
    

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    num_of_robots = 2
    clean_fraction = 80
    num_trials = 50
    
    # Defined room dimensions all of same surface area
    room_dimension = [(20,20),(25,16),(40,10),(50,8),(80,5),(100,4)]
    mean_times = []
    wToH_ratio = []
    
    # Simulate cleaning room with dimensions of room_dimension
    for room in range(len(room_dimension)):
        wToH_ratio.append(room_dimension[room][0]/room_dimension[room][1])
        mean_times.append(runSimulation(num_of_robots,1,room_dimension[room][0],room_dimension[room][1],clean_fraction/100,num_trials,StandardRobot))
    
    # Plot 
    plt.plot(wToH_ratio,mean_times,"bo")
    plt.ylabel('Mean time')
    plt.minorticks_off()
    plt.xlabel('Width/height')
    plt.title(f"Time to clean {clean_fraction}% of a room with different width/height ratio")
    plt.show()
    plt.close()
    

def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    # Instantiate 
    mean_times_stand = []
    mean_times_rand = []
    num_trials = 10
    WIDTH = HEIGHT = 20
    clean_fraction = 80
    NUM_ROBOTS = 15
    SPEED = 1
    robot_number = []
    # Simulate cleaning rooms with both types of robots from 1 to NUM_ROBOTS of robots
    for robot in range(1,NUM_ROBOTS + 1):
        robot_number.append(robot)
        mean_times_stand.append(runSimulation(robot,SPEED, WIDTH, HEIGHT,clean_fraction/100,num_trials,StandardRobot))
        mean_times_rand.append(runSimulation(robot,SPEED, WIDTH, HEIGHT,clean_fraction/100,num_trials,RandomWalkRobot))
        
    
    # Plot mean times
    plt.plot(robot_number,mean_times_stand,'bo-.', label = 'Standard Robot' )
    plt.plot(robot_number, mean_times_rand,'ro-.', label = 'Random walk robot')
    plt.legend(loc = 'best')
    plt.ylabel(f'Mean time with {num_trials} trials')
    plt.minorticks_off()
    plt.xlabel('Number of robots')
    plt.title(f"Time to clean {clean_fraction}% of a {WIDTH}x{HEIGHT} room")
    plt.show()

# Standard robot for a 20x20 room takes on average at most 1/2 time of Random walk robot
    # Which seems independet of the number of robots used to clean to room

showPlot1()
showPlot2()
showPlot3()