#!/usr/bin/env python

import sys
import rospy
import time
import os
from vpheno_srv.srv import Trigger
from insta_camera.srv import TriggerInsta
import logging

logging.basicConfig(filename="gamepad_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def takePicture():
	try:
		photo=rospy.ServiceProxy("shutter_trigger",Trigger)
		photo_insta=rospy.ServiceProxy("TriggerInsta", TriggerInsta)
		print ("Picture taken!!!!Inside takePicture function!!!!!!!!!!!!!!")
	except rospy.ServiceException, e:
		print e

if __name__=="__main__":
from inputs import get_gamepad
# TODO start time here
while True: 
    # TODO time now here
    # if time now - start time , more than 1 hour then break from while loop
    events = get_gamepad()
    for event in events:
#        print(event.ev_type, event.code, event.state  )
        if event.code in ['ABS_Z','ABS_RZ','BTN_TL','BTN_TR'] and event.state == 0:
            print('call trigger here')
            takePicture()
		
	# TODO
	# elif event.code in ['','']:
        #    break
		    
		
