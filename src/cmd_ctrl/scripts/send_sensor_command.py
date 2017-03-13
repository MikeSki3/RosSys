#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from robotHelpers.util import SonicSensorModule

ssm = SonicSensorModule.SonicSensor()
thresh = 20

def check_sensor():
    return ssm.distanceAverage()

def next_cmd():
    if(check_sensor() <= thresh):
        return 'a'
    else:
        return 'w'

def send_cmd():
    pub = rospy.Publisher('commander', String, queue_size=10)
    rospy.init_node('sender', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(next_cmd())
        rate.sleep()

if __name__ == '__main__':
    try:
        send_cmd()
    except rospy.ROSInterruptException:
        pass