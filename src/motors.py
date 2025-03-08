from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.button import Button
from ev3dev2.sensor.lego import TouchSensor

tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)
btn = Button()
ts = TouchSensor()

btn.wait_for_pressed('up')
tank_pair.on_for_rotations(left_speed=0, right_speed=50, rotations=5)
btn.wait_for_pressed('down')
tank_pair.on_for_rotations(left_speed=50, right_speed=0, rotations=5)
ts.wait_for_pressed()
tank_pair.on_for_degrees(left_speed=0, right_speed=50, degrees=720)
exit()