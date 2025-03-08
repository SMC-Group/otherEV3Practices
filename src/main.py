#!/usr/bin/env python3
from ev3dev2.button import Button
from ev3dev2.sound import Sound
btn = Button()
sound = Sound()

btn.wait_for_bump('left')
sound.beep()
btn.wait_for_pressed(['up', 'down'])
sound.beep()
btn.wait_for_released('right')
sound.beep()