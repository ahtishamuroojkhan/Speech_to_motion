from robot_controller import RobotController
import time

robot = RobotController()

time.sleep(2)

robot.get_pose()

time.sleep(2)

print("Base Left")
robot.base_left()
time.sleep(2)
robot.stop()

time.sleep(1)

print("Base Right")
robot.base_right()
time.sleep(2)
robot.stop()

time.sleep(1)

print("Shoulder Up")
robot.shoulder_up()
time.sleep(2)
robot.stop()

time.sleep(1)

print("Shoulder Down")
robot.shoulder_down()
time.sleep(2)
robot.stop()

print("Finished")
