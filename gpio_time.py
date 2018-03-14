import RPi.GPIO as GPIO
import numpy as np
import time

#Zaehlweise der Pins festlegen
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def measure_time():
    ch16, ch18, ch22 = (0,0,0)
    loop = True
    triggered_ch16, triggered_ch18, triggered_ch22 = (False, False, False)

    while loop == True:
        if GPIO.input(16) == GPIO.HIGH and triggered_ch16 == False:
            time_ch16 = time.clock()
            triggered_ch16 = True
        if GPIO.input(18) == GPIO.HIGH and triggered_ch18 == False:
            time_ch18 = time.clock()
            triggered_ch18 = True
        if GPIO.input(22) == GPIO.HIGH and triggered_ch22 == False:
            time_ch22 = time.clock()
            triggered_ch22 = True
        if (triggered_ch16, triggered_ch18, triggered_ch22) == (True, True, True):
            loop = False

    channel_times = (time_ch16, time_ch18, time_ch22)
    channel_times = np.asarray(channel_times)
    start_time = np.amin(channel_times)
    channel_times = channel_times - start_time

    print "Channel 16: {4}", channel_times[0], "Channel 18:", channel_times[1], "Channel 22", channel_times[2]
    time.sleep(0.4)
    return channel_times


while True:
    measure_time()
