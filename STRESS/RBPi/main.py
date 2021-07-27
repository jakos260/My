import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

while True:
	if (GPIO.input(20)):
		for i in range(3):
			GPIO.output(16, 1)
			time.sleep(0.1)
			GPIO.output(16, 0)
			time.sleep(0.1)
		break
	GPIO.output(16, 1)
	time.sleep(0.2)
	GPIO.output(16, 0)
	time.sleep(0.3)
