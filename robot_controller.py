import serial
import threading
import json
import time


class RobotController:

    def __init__(self, port="/dev/ttyUSB0", baudrate=115200):

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=1
        )

        self.ser.setRTS(False)
        self.ser.setDTR(False)

        self.last_pose = None
        self.pose_event = threading.Event()

        threading.Thread(
            target=self.read_feedback,
            daemon=True
        ).start()

        print("RoArm M2 Connected.")

    ####################################################
    # Read Robot Feedback
    ####################################################

    def read_feedback(self):

        while True:

            try:

                line = self.ser.readline().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                if line:

                    print("Robot:", line)

                    try:

                        data = json.loads(line)

                        # Robot pose feedback
                        if data.get("T") == 1051:

                            self.last_pose = data

                            self.pose_event.set()

                    except:
                        pass

            except Exception:

                break

    ####################################################
    # Send JSON Command
    ####################################################

    def send(self, data):

        message = json.dumps(data)

        print("Sending:", message)

        self.ser.write((message + "\n").encode())

        time.sleep(0.05)

    ####################################################
    # Get Robot Pose
    ####################################################

    def get_pose(self):

        self.pose_event.clear()

        self.send({"T": 105})

        if self.pose_event.wait(timeout=2):

            return self.last_pose

        return None

    ####################################################
    # Home
    ####################################################

    def home(self):

        self.send({"T": 100})

    ####################################################
    # Generic Motion
    ####################################################

    def move(self,
             axis,
             direction,
             speed=8,
             duration=0.5):

        self.send({
            "T": 123,
            "m": 0,
            "axis": axis,
            "cmd": direction,
            "spd": speed
        })

        time.sleep(duration)

        self.send({
            "T": 123,
            "m": 0,
            "axis": axis,
            "cmd": 0,
            "spd": 0
        })

    ####################################################
    # Base
    ####################################################

    def left(self):

        self.move(1, 1)

    def right(self):

        self.move(1, 2)

    ####################################################
    # Shoulder
    ####################################################

    def up(self):

        self.move(2, 2)

    def down(self):

        self.move(2, 1)

    ####################################################
    # Elbow
    ####################################################

    def forward(self):

        self.move(3, 2)

    def backward(self):

        self.move(3, 1)

    ####################################################
    # Wrist
    ####################################################

    def wrist_up(self):

        self.move(4, 2)

    def wrist_down(self):

        self.move(4, 1)

    ####################################################
    # Stop All Joints
    ####################################################

    def stop(self):

        for axis in [1, 2, 3, 4]:

            self.send({
                "T": 123,
                "m": 0,
                "axis": axis,
                "cmd": 0,
                "spd": 0
            })

            time.sleep(0.05)

    ####################################################
    # Close Port
    ####################################################

    def close(self):

        self.ser.close()