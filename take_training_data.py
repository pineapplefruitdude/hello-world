import RPi.GPIO as GPIO
import numpy as np
import time

#Zaehlweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

from gpio_time import measure_time

def training_loop():
    x = input("x Koordinate eingeben: ")
    y = input("y Koordinate eingeben: ")

    channel_times = measure_time()
    training_data = np.vstack((channel_times, x))
    training_data = np.vstack((training_data, y))
    print "training_data.shape ", training_data.shape

    np.savetxt("training_data", )

training_loop()
