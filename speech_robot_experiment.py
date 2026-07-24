import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from robot_controller import RobotController

import csv
import os
import time
from datetime import datetime

############################################################
# INITIALIZATION
############################################################

MODEL_PATH = "vosk-model-small-en-us-0.15"

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

robot = RobotController()

q = queue.Queue()

CSV_FILE = "speech_robot_results.csv"

############################################################
# CREATE CSV
############################################################

if not os.path.exists(CSV_FILE):

    with open(CSV_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Trial",
            "Date",
            "Time",
            "Command",
            "Recognized_Text",
            "Latency_ms",
            "X",
            "Y",
            "Z",
            "Base",
            "Shoulder",
            "Elbow",
            "Tool",
            "Success"
        ])

trial = 1

############################################################
# AUDIO CALLBACK
############################################################

def callback(indata, frames, time_info, status):

    if status:
        print(status)

    q.put(bytes(indata))

############################################################
# ROBOT COMMAND
############################################################

def execute_command(cmd):

    if cmd == "LEFT":
        robot.left()

    elif cmd == "RIGHT":
        robot.right()

    elif cmd == "UP":
        robot.up()

    elif cmd == "DOWN":
        robot.down()

    elif cmd == "FORWARD":
        robot.forward()

    elif cmd == "BACKWARD":
        robot.backward()

    elif cmd == "WRISTUP":
        robot.wrist_up()

    elif cmd == "WRISTDOWN":
        robot.wrist_down()

    elif cmd == "STOP":
        robot.stop()

    elif cmd == "HOME":
        robot.home()

############################################################
# START
############################################################

print("=" * 60)
print(" Offline Speech-Controlled RoArm-M2 Experiment")
print("=" * 60)

print("\nCommands")

print("LEFT")
print("RIGHT")
print("UP")
print("DOWN")
print("FORWARD")
print("BACKWARD")
print("WRISTUP")
print("WRISTDOWN")
print("STOP")
print("HOME")

print("\nPress CTRL+C to quit.\n")

############################################################

with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback):

    while True:

        data = q.get()

        if recognizer.AcceptWaveform(data):

            result = json.loads(recognizer.Result())

            text = result.get("text", "").strip().upper()

            if text == "":
                continue

            print("\nRecognized:", text)

            start = time.perf_counter()

            execute_command(text)

            pose = robot.get_pose()

            end = time.perf_counter()

            latency = round((end - start) * 1000, 2)

            if pose is None:

                success = "No"

                x = y = z = b = s = e = t = ""

            else:

                success = "Yes"

                x = pose.get("x", "")
                y = pose.get("y", "")
                z = pose.get("z", "")
                b = pose.get("b", "")
                s = pose.get("s", "")
                e = pose.get("e", "")
                t = pose.get("t", "")

            now = datetime.now()

            with open(CSV_FILE, "a", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    trial,
                    now.strftime("%Y-%m-%d"),
                    now.strftime("%H:%M:%S"),
                    text,
                    text,
                    latency,
                    x,
                    y,
                    z,
                    b,
                    s,
                    e,
                    t,
                    success
                ])

            print("Latency:", latency, "ms")

            if success == "Yes":

                print("Pose")

                print("X =", x)
                print("Y =", y)
                print("Z =", z)

            trial += 1