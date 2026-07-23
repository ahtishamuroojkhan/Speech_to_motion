import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from robot_controller import RobotController

MODEL_PATH = "vosk-model-small-en-us-0.15"

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model,16000)

robot = RobotController()

q = queue.Queue()

def callback(indata,frames,time,status):
    if status:
        print(status)

    q.put(bytes(indata))

print("="*50)
print("Speech Controlled RoArm M2")
print("Say:")
print("LEFT RIGHT UP DOWN")
print("FORWARD BACKWARD")
print("WRISTUP WRISTDOWN")
print("STOP")
print("="*50)

with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback):

    while True:

        data=q.get()

        if recognizer.AcceptWaveform(data):

            result=json.loads(recognizer.Result())

            text=result.get("text","").strip().upper()

            if text=="":

                continue

            print("\nRecognized:",text)

            ####################################################
            # Base
            ####################################################

            if text=="LEFT":

                robot.move(1,1)

            elif text=="RIGHT":

                robot.move(1,2)

            ####################################################
            # Shoulder
            ####################################################

            elif text=="UP":

                robot.move(2,2)

            elif text=="DOWN":

                robot.move(2,1)

            ####################################################
            # Elbow
            ####################################################

            elif text=="FORWARD":

                robot.move(3,2)

            elif text=="BACKWARD":

                robot.move(3,1)

            ####################################################
            # Wrist
            ####################################################

            elif text=="WRISTUP":

                robot.move(4,2)

            elif text=="WRISTDOWN":

                robot.move(4,1)

            ####################################################
            # Stop
            ####################################################

            elif text=="STOP":

                robot.stop()

            ####################################################
            # Current Pose
            ####################################################

            elif text=="POSE":

                robot.get_pose()

            ####################################################
            # Home
            ####################################################

            elif text=="HOME":

                robot.home()

            else:

                print("Unknown command")