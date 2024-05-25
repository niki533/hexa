import Adafruit_PCA9685
import time  

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

init_pwm0 = 300
init_pwm1 = 300
init_pwm2 = 300
init_pwm3 = 300

init_pwm4 = 300
init_pwm5 = 300
init_pwm6 = 300
init_pwm7 = 300

init_pwm8 = 300
init_pwm9 = 300
init_pwm10 = 300
init_pwm11 = 300

init_pwm12 = 300
init_pwm13 = 300
init_pwm14 = 300
init_pwm15 = 300

def singleServo(self, ID, direcInput, speedSet):
		self.wiggleID = ID
		self.wiggleDirection = direcInput
		self.scSpeed[ID] = speedSet
		self.scMode = 'wiggle'
		self.posUpdate()
		self.resume()

sc = singleServo()   # Instantiate the object that controls the servo
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
