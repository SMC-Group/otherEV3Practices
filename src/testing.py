#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor

ls = LargeMotor()
ls.on_for_rotations(speed=-60, rotations=5)
exit()