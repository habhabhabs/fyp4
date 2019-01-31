import snowboydecoder
import sys
import signal
import speech_recognition as sr
import os
from pynput.keyboard import Key, Controller
import time
import webbrowser

# initialise snowboy and pynput
print("Initialising Snowboy and Pynput...")
interrupted = False
keyboard = Controller()

# launch amazon sumerian
# assuming that the default browser is WebGL enabled (latest version of Chrome or Firefox)
print("Starting chatbot host interface...")
webbrowser.open_new("https://us-east-1.sumerian.aws/6f6b932453b5437fbeaa22ec916188cc.scene")


def hotwordCallback(fname):
    # start of keypress simulation
    
    # using pynput to hold space bar (only on ubuntu)
    keyboard.press(Key.space)
    t: int = 6 # hold for six seconds
    while t > 0: # between 0 and 6 seconds
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(("Holding space bar for: " + timeformat), end = '\r')
        time.sleep(1)
        t -= 1
    if t == 0: # when timeout, release spacebar
        keyboard.release(Key.space)
    time.sleep(1)

    # completion of execution (end of keypress simulation)
    t: int = 4 # cooldown period of four seconds between execution
    while t > 0:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(("Timeout before next press: " + timeformat), end = '\r')
        time.sleep(1)
        t -= 1



def detectedCallback():
  print('hotword triggered...', end='', flush=True)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.38)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=hotwordCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)

detector.terminate()




