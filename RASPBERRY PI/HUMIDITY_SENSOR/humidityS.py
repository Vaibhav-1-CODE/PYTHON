import RPi.GPIO as GPIO
import time
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT11
DHTOUT = 15  # GPIO Pin

GPIO.setmode(GPIO.BCM)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR, DHTOUT)
            if humidity is not None and temperature is not None:
                humidity = round(humidity, 2)
                temperature = round(temperature, 2)
                print('TEMPERATURE = {0:0.1f}*C  Humidity = {1:0.1f}%'.format(temperature, humidity))
            else:
                print("Cannot Connect to Sensor!")
            time.sleep(1)

    except KeyboardInterrupt:
        destroy()
