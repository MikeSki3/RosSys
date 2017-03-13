import RPi.GPIO as GPIO
import time
import sys

class SonicSensor:

    def __init__(self):
        self.TRIG = 20
        self.ECHO = 26
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
        GPIO.output(self.TRIG, False)
        time.sleep(2)

    def getDistance(self):
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        pulse_start = time.time()
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        # print("Distance: " + str(distance) + " cm")
        time.sleep(0.08)
        return distance

    def distanceLoop(self):
        try:
            while True:
                self.distanceAverage()
        except KeyboardInterrupt:
            GPIO.cleanup()

# Take 5 measurements and then calculate the average
    def distanceAverage(self):
        total = 0
        for i in range(5):
            total = total + self.getDistance()
            if (i == 4):
                print("Total: " + str(total))
                print("Distance: "  + str(total / 5) + " cm")
                return total / 5

    def cleanUp(self):
        GPIO.cleanup()