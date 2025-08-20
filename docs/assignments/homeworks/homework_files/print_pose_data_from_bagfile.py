import rclpy
from rclpy.node import Node

import sys
import numpy as np
import math
import utm

from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry

D2R = math.pi/180.0
R2D = 180.0/math.pi

latlon_outfile = open('lat_lon_data.txt', 'w')
utm_outfile = open('utm_data.txt', 'w')
angle_outfile = open('angle_data.txt', 'w')

def get_angle_from_quaternion(my_q):
    # this is for a planar problem, angle measured from x axis
    cos_half_ang = my_q.w
    sin_half_ang = my_q.z
    ang_rad = 2.0*math.atan2(sin_half_ang, cos_half_ang)
    return ang_rad

class CdcSubscriber(Node):

    def __init__(self):
        super().__init__('print_pose_data_from_bag')

        self.subscription_gps = self.create_subscription(
            NavSatFix, 'gps', self.gps_callback, 10)
        self.subscription_gps  # prevent unused variable warning

        self.subscription_odom = self.create_subscription(
            Odometry, 'odometry', self.odom_callback, 10)
        self.subscription_odom  # prevent unused variable warning

    def gps_callback(self, msg):

        self.get_logger().info(f'I heard: {msg.latitude} , {msg.longitude}')
        
        utmData = utm.from_latlon(msg.latitude, msg.longitude)
        
        print(f'{msg.latitude}, {msg.longitude}', file = latlon_outfile)
        print(f'{utmData[0]}, {utmData[1]}', file = utm_outfile)
    
    def odom_callback(self, msg):
        my_quat = msg.pose.pose.orientation
        ang_rad = get_angle_from_quaternion(my_quat)

        print(f'{my_quat.z}, {my_quat.w}, {ang_rad}', file = angle_outfile)
        

def main(args=None):
    rclpy.init(args=args)

    cdc_subscriber = CdcSubscriber()

    rclpy.spin(cdc_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    cdc_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()