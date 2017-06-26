#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import pygame.mixer
from gpiozero import MotionSensor
#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/pleasehold1.ogg")
#pygame.mixer.music.stop()
#pygame.mixer.music.set_volume(0)
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

pir = MotionSensor(4)                      #Associate pin 4 to PIR sensor

#Start never ending loop looking for motion
while True:
  #wait for motion detection
  pir.wait_for_motion()
  print "motion detected"
  #play audio file
  pygame.mixer.music.play()
  print "Playing audio clip"
  #wait for audio to finish playing
  while pygame.mixer.music.get_busy() == True:
    continue
  time.sleep(2)
  #wait for motion trigger to clear/reset
  pir.wait_for_no_motion()
