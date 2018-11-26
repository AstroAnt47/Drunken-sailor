"""
 This is a program of random walk and drunken sailors trying to get aboard
 before their ship leaves.

 Sailors start from a pub. They try to reach shore in 10 hours.
 They walk 100 meters in a minute. Every 100 meters they hit a crossroads
 and randomly selects a new direction. Sailors have a lifespan of 50 years.


y                                Shore (10,y)
|                               |
|                               |
|                               |
|                               |
| Pub (0,0)                     |
|#______________________________|________ x
|x=0                            |
|                               |
Every step is 100 meters (1 minute).
"""

from random import randint  # Import randint for randoming new direction.
from time import sleep      # Import pausing function from time package.
import numpy as np
import matplotlib.pyplot as plt


# Clearing output file:
tracked_path_file = open("Tracked_Path.txt","w").close()


# Print ASCII art
# Telling the user that program is running.
print "                                                             "
print "                                                             "
print "  ~~ Welcome to follow adventures of a Drunken Sailor. ~~    "
print "                                                             "
print "                       __#                                   "
print "                    _.'__#                                   "
print "                   [_.'  ##'\                                "
print "      _#                 # ) ')         _#                   "
print "    _'_##\               # )  ')      _'_##\                 "
print "   [_' # )\              # ')  ')    {_' # )\                "
print "       #{__)             #  )    )       # ) )               "
print "   ____#_____            #  )   .)       #{_/                "
print "  | ^^^^^^^^ \           # / __.)    ____#___                "
print "  | O O O O   \          #'''       / ^^^^^^ |=&===|====     "
print "  |__ ___      \_________#_________/  O O O  |&?=/ /')       "
print "     |           ^^^^^^^^^^^^^^^^^           /&   /  ')      "
print "     |        ______________________        /    {__-'       "
print "     |  ||   |#||#||#||#||#||#||#||#|      /                 "
print "~~~~~|~~||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.'~~~~~~~~~~~~~~~~  "
print " ~ ~ |__/'.______~_~_______~_~________..'   ~ ~       ~ ~    "
print "   ~ ~       ~ ~     ~ ~ ~       ~ ~     ~ ~      ~ ~        "
print "                                                             "
# Print the background story
print "Sailor has been drinking in a pub after long time sailing the seven \
seas. \nPub closes and the sailor has to find back to the ship. \n\
Sailor can't remember way back, but he/she is sure that ship will be found \n\
when the shore is found. Ship leaves in 10 hours, so sailor must hurry! \n\
Sailor has 50 years lifespan. If shore is not found in that time, you'd \n\
better call a gravedigger."
print " "
raw_input("Press Enter to continue...")




sleep(0.5)                    # Intelligent 0.5 sec pause.
print " "
mode = raw_input("How drunk the Sailor is? (Enter 'y'/'n'): ")
sleep(1)                    # Not so intelligent 1 sec thinking pause.
print " "

# If loop to decide the mode based on the answer.
if mode == "n":
    mode = "SAW"
    print "The Drunken Sailor has infinite amount of empty bottles. \n\
Sailor marks travelled path, so he/she won't cross the path. \n\
Clever isn't it? It could end up into a dead end though."
elif mode == "y":
    mode = "Full random"
    print "The Drunken Sailor will choose his/her route completely randomly.\n\
The Sailor won't recognize crossroads he/she has been earlier."
else:
    print "How drunk are you sailor? Come back when you are sober."
    exit()

print " "

n_Sailors = int(raw_input("Enter number of Sailors (Integer): "))
print " "
print " "



# Functions for converting units of the steps to years and kilometers.
def travel_time(time):
    if time >= 525600: # years
        time = time / 60. / 24. / 365. # Minutes to years
        return "%.2f years" % (time)
    elif time < 525600 and time >= 43200: # months
        time = time / 60. / 24. / 30 # Minutes to months
        return "%.2f months" % (time)
    elif time < 43200 and time >= 1440: # days
        time = time / 60. / 24. # Minutes to days
        return "%.2f days" % (time)
    elif time < 1440 and time >= 60: # hours
        time = time / 60.  # Minutes to hours
        return "%.2f hours" % (time)
    else:
        return "%.2f minutes" % (time) # minutes


def travel_distance(distance):
    distance *= 0.1 # Travelled distance from steps to kilometers
    return distance



# Direction randoming.
def random_new_direction(x, y, step):

    new_x = x
    new_y = y
    dice = randint(1, 4)
    if dice == 1:           # "north"
        new_y += 1

    elif dice == 2:         # "east"
        new_x += 1

    elif dice == 3:         # "south"
        new_y -= 1

    elif dice == 4:         # "west"
        new_x -= 1

    return [new_x, new_y]






def save_path(argument):
    # Save data and close file.
    tracked_path_file = open("Tracked_Path.txt", "a")
    tracked_path_file.write(argument)
    tracked_path_file.close()
    return

""" Function for saving results ("success" or "failure")
def save_results(steps, outcomes):
    # Save data and close file
    output_step_file = open("Result_Step.txt", "a")
    output_result_file.write(outcomes)
    output_step_file.write(steps)
    output_result_file.close()
    output_step_file.close()
    return
"""

def plot_path(filename):
    file = open(filename,"r")
    lines = file.readlines()
    file.close()
    x = []
    y = []
    for line in lines:
        coord = line.split()
        x.append(float(coord[0])*0.1) # Append x's in km
        y.append(float(coord[1])*0.1) # Append y's in km


    xcoords = np.array(x)
    ycoords = np.array(y)
    plt.plot(xcoords,ycoords)           # Plot route
    plt.plot(0,0, 'ro')
    plt.axis('equal')                # Set equal scaling
    plt.xlabel("km")                    # Set x-xlabel
    plt.ylabel("km")                    # Set y-label
    plt.axvline(x=10*0.1,color='k')     # Plot shore




    return



# Function that executes the random walk and prints the results.
def random_walk(sailor_position_x, sailor_position_y, mode):


    # Clear tracked path file for new sailor
    tracked_path_file = open("Tracked_Path.txt","w").close()

    sailor_position_x = 0    # Initial position of the Drunken Sailor, i.e. Pub
    sailor_position_y = 0    # Initial position of the Drunken Sailor, i.e. Pub
    path_history = "0 0 \n"  # History of path coordinates. [[step, x, y], ...]

    rip_age = 50 * 365 * 24 * 60 # Sailor dies at age of 50. [minutes]
    time_to_get_aboard = 1 * 60 * 10 # 10 hours to find the ship.
    step = 0                    # timestep
    result = " "                # Results for statistical analysis
    result_step = "0 \n"

    # Save data and close file.
    save_path(path_history)

    while step <= rip_age + 1:
        step += 1                               # Step counter
        if sailor_position_x != 10:
            position = random_new_direction(sailor_position_x, \
sailor_position_y, step)
            sailor_position_x = position[0]
            sailor_position_y = position[1]
            path_history = "%d %d \n" % (sailor_position_x, sailor_position_y)

            # Split the text file data into two arrays of coordinates.
            path = open("Tracked_Path.txt","r")
            lines = path.readlines()
            path.close()
            path_x = []
            path_y = []
            for line in lines:
                past_position = line.split()
                path_x.append(float(past_position[0]))
                path_y.append(float(past_position[1]))

            # Arrays of x and y coordinates in travelled path.
            past_x = np.array(path_x)
            past_y = np.array(path_y)

            # If Sailor is self avoiding
            if mode == "SAW":


                for k in range(len(path_x)):

                    if past_x[k] == sailor_position_x and \
past_y[k] == sailor_position_y:

                        print "Dead end! Sailor has walked here before. \n\
Better to follow the bottles back to the pub."
                        print "Bottle found at (%d, %d)." % \
(sailor_position_x, sailor_position_y)
                        print "Walked distance: %.1f km" % \
(travel_distance(step))
                        print "Travel time: %s" % (travel_time(step))
                        print " "
                        result = "Dead end \n"
                        result_step = "%d \n" % (step)


                        # Save data and close file
                        save_path(path_history)

                        plot_path("Tracked_Path.txt") # Plot path
                        return
            else:
                pass

            # Save data and close file
            save_path(path_history)


            # RIP Sailor
            if step == rip_age:
                print "R.I.P Drunken Sailor"
                print "You can find remains at (%d, %d)." % \
(sailor_position_x, sailor_position_y)
                print " "
                result = "RIP \n"
                result_step = "%d \n" % (step)
                break

        # If Sailor found the shore (== ship) in 10 hour, loop breaks.
        elif sailor_position_x == 10 and step <= time_to_get_aboard:
            print "Congratulations! Sailor found his/her way to shore in time."
            print "Walked distance: %.1f km" % (travel_distance(step))
            print "Travel time: %s" % (travel_time(step))
            print " "
            result = "Success \n"
            result_step = "%d \n" % (step)
            break

        # If Sailor reaches the shore, but it took longer than 10 hours,
        # this will be printed
        elif sailor_position_x == 10 and step > time_to_get_aboard:
            print "Sailor found the shore but ship has already left. \n\
Sailor ain't sailing anymore. Might as well head back to the pub."
            print "Walked distance: %.1f km" % (travel_distance(step))
            print "Travel time: %s" % (travel_time(step))
            print " "
            result = "Late \n"
            result_step = "%d \n" % (step)
            break




    plot_path("Tracked_Path.txt") # Plot path

    return






# Main:
for n in range(n_Sailors):
    n += 1
    sailor_x = 0    # Initial position of the Drunken Sailor, i.e. Pub
    sailor_y = 0

    random_walk(sailor_x, sailor_y, mode)




plt.show()




# The End
