#!/usr/bin/python
#encoding:utf-8

import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
import pygame.mixer
#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
#pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("pleasehold1.ogg")
#pygame.mixer.music.stop()
#pygame.mixer.music.set_volume(0)
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG = 21                                  #Associate pin 21 to TRIG
ECHO = 20                                  #Associate pin 20 to ECHO

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  #print "Waitng For Sensor To Settle"
  time.sleep(0.5)                            #Delay of 1/2 second

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 
    if pulse_end - pulse_start > 0.5:
      break;

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance)            #Round to two decimal points

  if distance is None or distance < 2 or distance > 400:
    print "out of range"
    distance = 0
    pygame.mixer.music.play()
    print "Playing audio clip"
    while pygame.mixer.music.get_busy() == True:
      continue
    time.sleep(2)
  else:
    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
    if distance > 50:
      pygame.mixer.music.play()
      print "Playing audio clip"
      #pygame.mixer.music.set_volume(1)
      while pygame.mixer.music.get_busy() == True:      
        continue
      #pygame.mixer.music.stop()
      #pygame.mixer.music.set_volume(0)
      time.sleep(2)
