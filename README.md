# Motion detector with audio prompt to hold onto a hand railing.

## Now using a motion PIR sensor! For the old HC-SR04 sonar sensor scroll to the bottom

### Parts needed:
* Raspberry pi
* PIR motion sensor
* Speaker (for 3.5mm audio out)


### Installation:
* Install the PIR sensor signal pin to pi pin 4
* Install the PIR sensor vcc to a +5v and gnd to a ground pin
* Connect your speaker to the pi via the 3.5mm audio jack
* Run motion.py, be sure to keep the audio .ogg file in the same folder as motion.py

#### Run on boot:
* Insert (sleep 10;python /home/pi/motion.py)&  into /etc/rc.local just before exit 0
* Where /home/pi/ is the directory you have the motion script located

### Running:
* The pi will continuously scan via the PIR motion sensor for changes
* When motion is detected (like a door being opened) the audio clip will play
* The pi will wait for ~3 seconds after playing the audio clip before resuming its motion sensor scanning
* The audio file can be any .ogg file, but must have the same name as the original




## OLD!! Written for the raspberry pi using the 3.5mm audio jack and HC-SR04 sonar sensor

### Parts needed:
* Raspberry pi
* HC-SR04 sonar sensor
* 10k ohm resistor
* Speaker (for 3.5mm audio out)


### Installation:
* Install the 10kohm resistor between the echo pin on the HC-SR04 sensor and pi pin 20
* Install the HC-SR04 trig pin to pi pin 21
* Install the HC-SR04 vcc to a +5v and gnd to a ground pin
* Connect your speaker to the pi via the 3.5mm audio jack
* Run sonar2.py, be sure to keep the audio .ogg file in the same folder as sonar2.py

### Run on boot:
* Insert (sleep 10;python /home/pi/sonar2.py)&  into /etc/rc.local just before exit 0
* Where /home/pi/ is the directory you have the sonar2 script located

### Running:
* The pi will continuously scan via the sonar sensor for distance changes
* When a large distance change is detected (like a door being opened) the audio clip will play
* The pi will wait for ~3 seconds after playing the audio clip before resuming its sonar sensor scanning
* The audio file can be any .ogg file, but must have the same name as the original
