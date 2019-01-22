# Gesture Recognition script for SIT@NYP Interactive Public Display
Developed on Python 3.6 ('python-3.6`) using the following libraries:
  - pynput (`pip3 install pynput`) - keyboard and mouse emulator
  - cv2 (`sudo apt-get install python-opencv` on Ubuntu) - OpenCV engine (ensure that it is on version 3.2.0)
  - numpy - dependency for cv2
  
To minimise compatability issues, try to keep executions in Python 3.6 
- `py -3.6 -m pip install pynput`
- `py -3.6 -m pip install opencv-python==3.2.0.8` (or can use `apt-get` for Ubuntu)
- `py -3.6 -m pip install numpy` (dependency for `opencv-python`)

## Changelog:
Version 2: 22 January 2019
- Verified that full functionality works with Ubuntu, and basic functionality to work on Windows.

Version 1: 20 January 2019
- ensuring OpenCV works by generating a windowed output upon running script.
- initial release

