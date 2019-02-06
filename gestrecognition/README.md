# Gesture Recognition script for SIT@NYP Interactive Public Display
Developed on Python 3.6 ('python-3.6`) using the following libraries:
  - pynput (`sudo pip3 install pynput`) - keyboard and mouse emulator (for Ubuntu)
  - cv2 (`sudo apt-get install python-opencv` on Ubuntu) - OpenCV engine (ensure that it is on version 3.2.0)
  - numpy - dependency for cv2
  - wmctrl (`sudo pip3 install wmctrl` and `sudo apt install wmctrl`) - to keep the webcam output always on top (for Ubuntu OS)
  
To minimise compatability issues, try to keep executions in Python 3.6 
- `sudo py -3.6 -m pip install pynput`
- `sudo py -3.6 -m pip install opencv-python==3.2.0.8` (or can use `apt-get` for Ubuntu)
- `sudo py -3.6 -m pip install numpy` (dependency for `opencv-python`)
- `sudo py -3.6 -m pip install wmctrl` 

How the gesture regognition works:
- Upon running the gesture script, a window containing the camera output will appear.
- The detection area of gestures only work inside of the green rectangle box.
- Wave inside the green box to invoke a spacebar hold.
- Once detected, the script will hold the spacebar for six seconds.
- Following which, there is a cooldown period (thread sleep) of four seconds before the next wave.

Operating Requirements:
- Python 3.6
- OpenCV 3.2
- Ubuntu 18.04

## Changelog:
Version 3: 1 Feb 2019
- Dropped Windows support in favour of integrating with Snowboy Hotword Detection (only \*nix supported)
- Ubuntu as core operating requirement rather than an option

Version 2.1: 23 January 2019
- Added `sys.platform` flags to check if current application runs on Linux `linux` or Win10 `win32`.
- Hold space bar upon wave works on Ubuntu, but the drivers involved for Windows still on fix (issue 662 in pywinauto github) https://github.com/pywinauto/pywinauto/issues/662
- Using `pynput` for Ubuntu, and using `pywinauto` for Windows (current plan, might change).

Version 2: 22 January 2019
- Verified that full functionality works with Ubuntu, and basic functionality to work on Windows.

Version 1: 20 January 2019
- ensuring OpenCV works by generating a windowed output upon running script.
- initial release

