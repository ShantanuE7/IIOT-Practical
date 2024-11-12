import RPi.GPIO as GPIO
import time
import requests

# Set up GPIO pins
TRIG = 14 
ECHO = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(2)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance

try:
    while True:
        distance = measure_distance()
        print(f"Distance: {distance} cm")
        
        try:
            response = requests.post('http://172.16.10.69:5000/update', json={'distance': distance})
            print("Data sent to ESP32:", response.text)
        except requests.exceptions.RequestException as e:
            print("Error sending data to ESP32:", e)

        time.sleep(0.5)
finally:
    GPIO.cleanup()
