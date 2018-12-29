#!/usr/bin/env python
import rospy
from sensor_msgs.msg import NavSatFix
from std_msgs.msg import Int32
import geopy.distance
import math
from auto_navi.msg import try1, try3
import time
#import message_filters





'''
global a


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "\nGPS:\nLat: [{}]\nLong: [{}]\nAlti: [{}]".
    #format(data.latitude, data.longitude, data.altitude))
    dist_cal(data.latitude, data.longitude)
def callback1(data1):
   
    #turning_ws(data)
    
    a= data1
    
    return a.data
    #print a.data
     
'''
'''
def turning_ws(data):
    cHDG=data
    return cHDG
'''
'''    

def dist_cal(a,b):
    coords_1 = (a, b)
    coords_2 = (x, y)
    dist= geopy.distance.distance(coords_1, coords_2).m
    #goal heading
    gHDG= math.atan2((x-a),(y-b))
    gHDG= math.degrees(gHDG)
    print gHDG
    #current heading 
    #msg=Float64()
    cHDG= a.data
    print a.data
    #angle to be turn
    if (gHDG-cHDG)>180:
     dHDG= gHDG-360-cHDG
     print dHDG
     pub.publish(dHDG)
    if (gHDG-cHDG)<-180:
     dHDG= 360-cHDG+gHDG
     print dHDG
     pub.publish(dHDG)


    


def gyros():
    rospy.init_node('gpps', anonymous=True)
    rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
    rospy.Subscriber("/mavros/global_position/compass_hdg", Float64, callback1)
    pub= rospy.Publisher("turning_cmd", Float64, queue_size=10)
    rospy.spin()
'''
'''
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "\nGPS:\nLat: [{}]\nLong: [{}]\nAlti: [{}]".
    #format(data.latitude, data.longitude, data.altitude))
    dist_cal(data.latitude, data.longitude)
    print data.latitude
'''


#def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + "\nGPS:\nLat: [{}]\nLong: [{}]\nAlti: [{}]".
    #format(data.latitude, data.longitude, data.altitude))
#    dist_cal(data.latitude, data.longitude)

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "\nGPS:\nLat: [{}]\nLong: [{}]\nAlti: [{}]".
    #format(data.latitude, data.longitude, data.altitude))
    msg=try3()
    msg.lat= data.latitude
    msg.long= data.longitude
    pub.publish(msg)
  


def gyros():
    rospy.init_node('gpps', anonymous=True)
    rospy.Subscriber("/mavros/global_position/global", NavSatFix, callback)
    pub= rospy.Publisher("coordinates1", try3, queue_size=10)
    #rospy.Subscriber("/mavros/global_position/compass_hdg", Float64, callback1)
    #gps= message_filters.Subscriber("/mavros/global_position/global", NavSatFix)
    #coordinates=message_filters.Subscriber("coordinates1", try3)
    #ts= message_filters.TimeSynchronizer([gps,coordinates], 10)
    #ts.registerCallback(callback)
    rospy.spin()
    

if __name__ == '__main__':
    print "started!!"
    #pub= rospy.Publisher("turning_cmd", Int32)
    x = float(raw_input('latitude: '))
    y =float(raw_input('longitude: '))
    gyros()

