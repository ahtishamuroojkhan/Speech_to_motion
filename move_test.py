from robot_controller import RobotController
import time

robot = RobotController()

time.sleep(2)

# ---------------------------------
# Generic movement function
# ---------------------------------
def move(axis, direction, speed=8, duration=0.5):

    print(f"\nMoving Axis={axis}, Direction={direction}")

    robot.send({
        "T": 123,
        "m": 0,
        "axis": axis,
        "cmd": direction,
        "spd": speed
    })

    time.sleep(duration)

    robot.send({
        "T": 123,
        "m": 0,
        "axis": axis,
        "cmd": 0,
        "spd": 0
    })

    time.sleep(1)


#########################################################
# CHANGE ONLY THESE VALUES FOR TESTING
#########################################################

#move(1, 1)      # Base Left

#move(1,2)     # Base Right

#move(2,1)     # Shoulder Up

#move(2,2)     # Shoulder Down

#move(3,1)     # Elbow Up

#move(3,2)     # Elbow Down

#move(4,1)     # Wrist Up

move(4,2)     # Wrist Down

#########################################################

robot.close()