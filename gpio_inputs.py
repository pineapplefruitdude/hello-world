import RPi.GPIO as GPIO
import time

#Zaehlweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def measure_time():
    i = 0
    j = 0
    start_time = 0
    a = True
    while a == True:
        if GPIO.input(18) == GPIO.HIGH:
            start_time = time.clock()
        if GPIO.input(16) == GPIO.HIGH:
            end_time = time.clock
            a = False
    delay = end_time - start_time
    print "delay [s] ", delay
    
        """
        if GPIO.input(18) == GPIO.HIGH:
            channel18 = 1
            i = i+1
        if GPIO.input(18) == GPIO.LOW:
            channel18 = 0

        if GPIO.input(16) == GPIO.HIGH:
            channel16 = 1
            j = j+1
        if GPIO.input(16) == GPIO.HIGH:
            channel16 = 0

        if i > 10 and j <= 10 and start_time == 0:
            start_time = time.clock()
        if j > 10 and i <= 10 and start_time == 0:
            start_time = time.clock()
        if i > 10 and j > 10:
            end_time = time.clock()
            delay = end_time - start_time
            print "delay [s]", delay
            a = False
        """
while True:
    measure_time()
