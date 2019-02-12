#!/usr/bin/env bash

/usr/bin/python3 sumerian.py &

/usr/bin/python3 hotword/voicerecognition.py hotword/alexa_02092017.umdl &

/usr/bin/python3 gestrecognition/handrecog_input.py &
