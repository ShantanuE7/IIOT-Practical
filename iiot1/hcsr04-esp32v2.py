import RPi.GPIO as GPIO
import time
import socket

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

    pulse_start = time.time()
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    pulse_end = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

# Set up the socket connection
receiver_ip = '172.16.10.41'  # Replace with the receiver's IP
PORT = 5000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((receiver_ip, PORT))
        while True:
            distance = measure_distance()
            print(f"Distance: {distance} cm")
            message = f"{distance}\n"  # Prepare the message
            s.sendall(message.encode('utf-8'))  # Send data
            time.sleep(0.5)
finally:
    GPIO.cleanup()
