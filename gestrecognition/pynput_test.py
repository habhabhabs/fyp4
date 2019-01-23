from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.space)
while True:
    pass
keyboard.release(Key.space)
print("end printing.")

