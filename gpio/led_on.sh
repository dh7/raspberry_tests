#!/bin/bash

#init the pin 17 in out mode
gpio -g mode 17 out

#turn on the led
gpio -g write 17 1
