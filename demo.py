import RPi.GPIO as GPIO
import time

sensor_pin = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(sensor_pin):
              print("No Object")
              while GPIO.input(sensor_pin):
                   time.sleep(0.2)
        else:
               print("Detect Object") <-call API Camera

except KeyboardInterrupt:
     GPIO.cleanup()
     print("KeyboardInterrupt") 
