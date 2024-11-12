import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

def generate_sensor_data(num_samples=1000):
    np.random.seed(42) 
    timestamps = pd.date_range(start='2023-01-01', periods=num_samples, freq='H')
    temperature = np.random.normal(loc=25, scale=5, size=num_samples)  # Average 25°C
    humidity = np.random.normal(loc=60, scale=10, size=num_samples)    # Average 60%
    pressure = np.random.normal(loc=1013, scale=10, size=num_samples)  # Average 1013 hPa
    
    data = pd.DataFrame({
        'timestamp': timestamps,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure
    })
    return data


def analyze_data(data):
    print("Basic Statistics:")
    print(data.describe())

    correlation = data.corr()
    print("\nCorrelation Matrix:")
    print(correlation)

    X = data[['temperature', 'humidity']]
    y = data['pressure']
    model = LinearRegression()
    model.fit(X, y)

    print(f"\nLinear Regression Coefficients: {model.coef_}")

    
    data['predicted_pressure'] = model.predict(X)

    return correlation


def visualize_data(data):
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    sns.lineplot(data=data, x='timestamp', y='temperature', color='orange')
    plt.title('Temperature Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')

    plt.subplot(3, 1, 2)
    sns.lineplot(data=data, x='timestamp', y='humidity', color='blue')
    plt.title('Humidity Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Humidity (%)')

    plt.subplot(3, 1, 3)
    sns.lineplot(data=data, x='timestamp', y='pressure', label='Actual Pressure', color='green')
    sns.lineplot(data=data, x='timestamp', y='predicted_pressure', label='Predicted Pressure', color='red')
    plt.title('Actual vs. Predicted Pressure')
    plt.xlabel('Timestamp')
    plt.ylabel('Pressure (hPa)')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    sensor_data = generate_sensor_data()

    correlation = analyze_data(sensor_data)

    visualize_data(sensor_data)

if __name__ == "__main__":
    main()
