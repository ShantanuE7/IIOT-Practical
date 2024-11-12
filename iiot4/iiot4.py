import os
import time
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import board
import adafruit_dht
 
sensor = adafruit_dht.DHT11(board.D15) 
def read_temp():
    
    Condition=True
    while Condition:
        try:
        # Print the values to the serial port
            temperature_c = sensor.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = sensor.humidity
            print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        
        
        
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error

        time.sleep(2.0) 
        return temperature_c


times = []
temperatures = []

def log_temperature():
    csv_file = 'temperature_data.csv'
    
    # Create or open the CSV file and write the header if it's new
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow(['Timestamp', 'Temperature (°C)'])

        while True:
            temp = read_temp()
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"{timestamp}: Current Temperature: {temp} °C")
            
            # Write the data to the CSV file
            writer.writerow([timestamp, temp])
            file.flush()  # Ensure data is written to file
            
            # Store data for visualization
            times.append(timestamp)
            temperatures.append(temp)
            
            time.sleep(10)  # Log data every minute

def update_plot(frame):
    plt.clf()  # Clear the current figure
    plt.plot(times, temperatures, label='Temperature (°C)', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Real-time Temperature Monitoring')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

if __name__ == "__main__":
    import threading

    # Start the logging in a separate thread
    log_thread = threading.Thread(target=log_temperature)
    log_thread.daemon = True
    log_thread.start()

    # Set up the plot
    plt.figure()
    ani = FuncAnimation(plt.gcf(), update_plot, interval=1000)  # Update plot every second
    plt.show()

