#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(180)
red = (255, 0, 0)

humidity = sense.humidity
print (int(humidity));
sense.show_message(str(int(humidity)), text_colour=red,scroll_speed=0.7)
