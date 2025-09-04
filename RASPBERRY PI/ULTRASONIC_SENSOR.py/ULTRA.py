import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

TRIG_PIN = 15
ECHO_PIN = 14

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Ensure trigger is low
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.0002)

    # Send 10us pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for echo start
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Wait for echo end
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Convert to distance (speed of sound = 34300 cm/s)
    distance = pulse_duration * 34300 / 2
    return distance

try:
    while True:
        dist = get_distance()
        print(f"Distance: {dist:.2f} cm")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user")
    GPIO.cleanup()
