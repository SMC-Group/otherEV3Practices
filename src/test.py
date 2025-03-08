#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound
btn = Button()
sound = Sound()

while btn.any():
    sound.beep()
    exit()