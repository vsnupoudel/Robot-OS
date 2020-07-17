#!/usr/bin/env python

import sys
import rospy
import time
import os
from vpheno_srv.srv import Trigger
from insta_camera.srv import TriggerInsta
from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG
, format='%(asctime)s: %(message)s')

def takePicture():
	try:
		photo=rospy.ServiceProxy("shutter_trigger",Trigger)
		resp=photo()
		photo_insta=rospy.ServiceProxy("TriggerInsta", TriggerInsta)
		resp_insta = photo_insta()

		#os.system('./a.out 0')
		#os.system('./a.out 1')
		print ("Picture taken!!!!Inside takePicture function!!!!!!!!!!!!!!")
		return resp
	except rospy.ServiceException, e:
		print e

def on_click(x, y, button, pressed):
    if pressed:
	logging.info('Inside the on_click')
        print('Inside the on_click')
        takePicture()

if __name__=="__main__":
	#print ("How much time ?")
	#sec = int(raw_input())
	#kb=open("/dev/input/js0")
	rospy.wait_for_service("shutter_trigger")
	rospy.wait_for_service("TriggerInsta")
	with Listener(on_click=on_click) as listener:
	    listener.join()

		    
		