#!/usr/bin/env python

from util import Robot

c=0
speed = 150
period = .10
forward = False
backward = False
LEFT_TRIM = 0
RIGHT_TRIM = -7
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

def move(command):
	if command == 'w':
		print("FORWARD")
		robot.forward(speed)
	elif command == 'a':
		print("LEFT")
		robot.left(speed)
	elif command == 's':
		print("BACKWARD")
		robot.backward(speed)
	elif command == 'd':
		print("RIGHT")
		robot.right(speed)


0
