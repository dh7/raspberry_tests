#!/bin/bash

#init the pin 17 in out mode
gpio -g mode 17 out

#turn off the led
gpio -g write 17 0