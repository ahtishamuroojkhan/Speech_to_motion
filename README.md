# Speech-to-Motion: Embedded Offline Speech-Controlled Robotic Manipulator

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%205-green.svg)]()
[![Speech Recognition](https://img.shields.io/badge/Vosk-Offline%20ASR-orange.svg)]()


This repository contains the implementation of an **embedded offline speech-controlled robotic manipulator** using a **Raspberry Pi 5**, **Vosk Offline Automatic Speech Recognition (ASR)**, and the **Waveshare RoArm-M2** robotic manipulator.

The proposed framework performs **completely offline speech recognition**, eliminating the need for cloud-based speech processing while enabling reliable, privacy-preserving, and low-latency voice control of a robotic manipulator.

---

# Features

- Offline speech recognition using Vosk
- Real-time embedded implementation on Raspberry Pi 5
- JSON-based robot motion control
- USB serial communication with RoArm-M2
- Continuous robot pose feedback
- Experimental data logging
- Reproducible experimental evaluation

---

# System Overview

The system consists of two software modules:

## 1. speech_robot.py

Responsible for

- Audio acquisition
- Offline speech recognition
- Voice command extraction
- Command validation
- Command mapping

Supported commands

- LEFT
- RIGHT
- UP
- DOWN
- FORWARD
- BACKWARD
- WRISTUP
- WRISTDOWN
- HOME
- POSE
- STOP

---

## 2. robot_controller.py

Responsible for

- JSON motion generation
- USB serial communication
- Robot motion execution
- Pose acquisition
- Joint-angle feedback
- Experimental data logging

---

# Repository Structure

```text
Speech_to_motion/
│
├── README.md
├── speech_robot.py
├── robot_controller.py
├── speech_robot_experiment.py
├── speech_robot_results.csv
├── speech_robot_results.txt
├── speech_test.py
├── move_test.py
├── joint_test.py
```

---

# Hardware Requirements

- Raspberry Pi 5
- Waveshare RoArm-M2
- Logitech C270 USB Camera (microphone)
- USB Serial Interface
- Raspberry Pi OS (64-bit)

---

# Software Requirements

- Python 3.11
- Vosk
- SoundDevice
- PySerial

Install the required packages

```bash
pip install vosk
pip install sounddevice
pip install pyserial
```

Download the Vosk English model

```
vosk-model-small-en-us-0.15
```

from

https://alphacephei.com/vosk/models

Extract the model into the project directory.

---

# Running the System

Start the speech-controlled robotic manipulator

```bash
python speech_robot.py
```

For experimental data collection

```bash
python speech_robot_experiment.py
```

---

# Experimental Dataset

The repository contains the experimental dataset used in the paper.

```
speech_robot_results.csv
```

The dataset contains

- Trial Number
- Expected Command
- Recognized Command
- Recognition Accuracy
- Command Latency
- Cartesian Position (X,Y,Z)
- Base Joint
- Shoulder Joint
- Elbow Joint
- Tool Joint

---

# Reproducing the Results

The experimental results reported in the paper can be reproduced using the publicly available Kaggle notebook.

1. Download

```
speech_robot_results.csv
```

from this repository.

2. Open the Kaggle notebook

https://www.kaggle.com/code/mechasoftskills/speech-to-motion-results

3. Upload

```
speech_robot_results.csv
```

4. Execute all notebook cells.

The notebook automatically reproduces

- Speech recognition accuracy
- Command execution latency
- End-effector trajectory
- Joint-angle variation
- Experimental figures

---

# Experimental Performance

The proposed system achieved

| Metric | Result |
|---------|--------|
| Speech Recognition Accuracy | **94.05%** |
| Average Command Latency | **657.5 ms** |
| Speech Recognition | Offline |
| Internet Required | No |

---

# Citation

If you use this repository in your research, please cite the associated publication.

```bibtex
@misc{SpeechToMotionGitHub,
  author       = {Ahtisham Urooj Khan},
  title        = {Speech\_to\_motion: Embedded Offline Speech-Controlled Robotic Manipulator},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/ahtishamuroojkhan/Speech_to_motion}}
}
```

---

# Paper

The implementation accompanies the research paper

**An Embedded Offline Speech Recognition Framework for Real-Time Voice-Controlled Robotic Manipulation**

---

# Author

**Ahtisham Urooj Khan**

PhD. Systems and Control Engineering

King Fahd University of Petroleum and Minerals (KFUPM)

GitHub

https://github.com/ahtishamuroojkhan

---
