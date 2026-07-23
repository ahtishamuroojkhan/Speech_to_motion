import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-en-us-0.15"

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

print("===================================")
print(" Offline Speech Recognition Started")
print(" Press Ctrl+C to Stop")
print("===================================")

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

            text = result.get("text", "").strip()

            if text:
                print("Recognized:", text)
