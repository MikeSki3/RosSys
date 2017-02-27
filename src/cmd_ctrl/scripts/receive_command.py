#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from robotHelpers import commander

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    commander.move(data.data)

def receiver():
    rospy.init_node('receiver', anonymous=True)

    rospy.Subscriber("commander", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    receiver()
