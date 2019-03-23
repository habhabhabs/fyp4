<!-- This is a Markdown file. Please use a Markdown viewer to optimally view readme (with hyperlinks) -->
# fyp4-interactive-display
The directory contains the following files:
- [`application`](application/)
  - contains the (stable) Python files required to drive the display. 
  - To run the program, execute [this Bash script](application/exec.sh).
  - To modify the link of the Amazon Sumerian project, [change this file](application/sumerian.py).
  - Main source code files to take note:
    - [Gesture Recognition](application/gestrecognition/handrecog_input.py) - the script to drive the gesture recognition. 
      - Important things to note is the HSV values (amount of light to capture) and the VideoCapture input (camera selection of either 0 or 1, depending on hardware). Readme file for Gesture Recognition [here](application/gestrecognition/README.md).
    - [Hotword Detection](application/hotword/voicerecognition.py) - Readme file for Hotword Detection [here](application/hotword/README.md).
- [`development`](development/) 
  - contains source code used for development and setup files needed to `make` (compile) the `snowboy` and `opencv` binaries.
  - **To install OpenCV**, please run [this Bash script](development/gestrecognition/opencv-install.sh).
  - **To install Snowboy**, please see [this guide](development/hotword/install-snowboy/README.md).
- [`backup`](backup/)
  - contains bundles for Amazon Sumerian and Amazon Lex.
  - For [**Amazon Sumerian**](backup/sumerian/FINAL)
    - create an empty scene in your Sumerian account and import the zip bundle by using 'Import Assets' in menu bar. (guide credits to: https://www.andreasjakl.com/download-export-or-backup-amazon-sumerian-scenes-part-6/)
    - Use the default Amazon Cognito Pool template to link both Lex and Sumerian up. (guide credits to: https://docs.sumerian.amazonaws.com/tutorials/create/beginner/dialogue-component/)
    - Do also ensure that Amazon Polly is linked up to Cognito Pool as well!
  - For [**Amazon Lex**](backup/lex/FINAL)
    - Import the entire zip file containing a JSON file into Lex directly. A set of Intents (skills) will then be transferred to your account. You may create an empty chatbot and import the intents manually. Please refer to https://docs.aws.amazon.com/lex/latest/dg/import-export-lex.html for the full set of import/export instructions.

Please refer to the README.md files located in every folder (`application`, `development` and `backup`) if you need more details. Thank you!

Dissertation repo for this project, please clone/fork: https://github.com/habhabhabs/fyp4-interactive-dissertation

FYP Project of Ng Kim Meng 2355364N \
SIT@NYP Interactive Public Display
