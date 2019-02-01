# Hotword Detection (Trigger Word Switch) for SIT@NYP Interactive Public Display
---
Developed on Python 3.6 `python-3.6` using the following libraries:
- pynput (pip3 install pynput) - keyboard and mouse emulator (for Ubuntu)
- snowboy (build from source - instructions provided) - Snowboy Hotword Detection engine 

To minimise compatibility issues, try to keep executions in Python 3.6.
- py -3.6 -m pip install pynput
- Instruction to build Snowboy [here.](install-snowboy/install-instructions.md)

Operating Requirements:
- Python 3.6
- Compiled binaries for Snowboy
- Ubuntu 18.04 (`snowboy` *only* works in *nix systems)

Instructions:
- In this directory, run `python3 voicerecognition.py Neo-ya.pmdl` ("Neoya" is the trigger keyword for the chatbot), or
  - `python3 voicerecognition.py resources/alexs/alexs_02092017.umdl` ("Alexa" is the trigger keyword for the chatbot)

# Changelog:
Version 1: 30 Jan 2019
- Added 'Neo-ya' model as an example. But can use 
