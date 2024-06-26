import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = []

def on_message(client, userdata, message):
    print("Message received:")
    payload = str(message.payload.decode("utf-8"))
    data.append((datetime.now(), payload))
    print("Checking Data size: ", len(data))
    if len(data) > 100:
        data.pop(0)
    
    # Converting data list to DataFrame for processing
    df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
    df["temperature"] = df["sensor_data"].apply(lambda x: eval(x)["temperature"])
    df["humidity"] = df["sensor_data"].apply(lambda x: eval(x)["humidity"])

    print("Dataframe:")
    print(df)
    
    plt.clf()  # Clear the current figure
    plt.plot(df["timestamp"], df["temperature"], label="Temperature")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity")
    plt.legend()
    plt.draw()
    plt.pause(0.1)  # Pause briefly to update the plot

# Setting up the MQTT client
client = mqtt.Client()
print("Connecting to MQTT broker...")
client.on_message = on_message  # Register the message callback
client.connect("localhost", 1883)  # Connect to the MQTT broker
client.subscribe("sensor/data")  # Subscribe to the sensor data topic

plt.ion()  # Turn on interactive plotting
plt.figure()  # Create a new figure

client.loop_start()  # Start the network loop in a non-blocking way

# Use try-except to keep the plot window open until manually closed
try:
    plt.show()
except KeyboardInterrupt:
    print("Plotting stopped by user.")

client.loop_stop()  # Stop the MQTT loop when done
