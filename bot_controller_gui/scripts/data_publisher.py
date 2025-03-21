#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist


battery = 100

def velocity(msg):
    global battery
    
    if msg.linear.x != 0 or msg.angular.z != 0:
        battery -= 1
    pub = rospy.Publisher("rover_stats", Float32MultiArray, queue_size=10)
    stat = Float32MultiArray()
    stat.data = [battery, msg.linear.x, msg.angular.z]
    pub.publish(stat)


if __name__ == "__main__":
    rospy.init_node("data_publisher", anonymous=False)
    sub = rospy.Subscriber("/cmd_vel", Twist, velocity)

    rospy.spin()