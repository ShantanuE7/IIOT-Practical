# Based on Adafruit_CircuitPython_DHT Library Example

import time
import board
import adafruit_dht
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'shantanuekad2021.ainds@mmcoe.edu.in'
password = 'qigf vctw vnse zlpj'  # Replace with the App Password you generated

# Email details
from_addr = 'shantanuekad2021.ainds@mmcoe.edu.in'
to_addr = 'ekadshantanu@gmail.com'
subject = 'No subject'
body = 'help SOS :-[ .Sensor value upp.'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))


# Sensor data pin is connected to GPIO 4
#sensor = adafruit_dht.DHT22(board.D4)
# Uncomment for DHT11
sensor = adafruit_dht.DHT11(board.D14)
Condition=True
while Condition:
    try:
        # Print the values to the serial port
        temperature_c = sensor.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensor.humidity
        print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
    
        if temperature_c>=35:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)
            server.send_message(msg)
            print('Email sent successfully!')
            server.quit()
            Condition=False
    
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3.0) 
