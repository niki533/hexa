import Adafruit_PCA9685
import time  

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

sc = RPIservo.ServoCtrl()   # Instantiate the object that controls the servo
sc.start()  # Start this thread, when the servo does not move, the thread is suspended

def stopWiggle(self):
		self.pause()
		self.posUpdate()

while 1:  
	sc.singleServo(3, -1, 2)      
	time.sleep(1)  
	sc.stopWiggle()     
	sc.singleServo(3, 1, 2)  
	time.sleep(1)  
	sc.stopWiggle()  
