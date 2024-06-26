import paho.mqtt.client as mqtt
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime 
import time


data = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor/data")

def on_message(client, userdata, msg):
    print(f"Received '{msg.payload.decode()}' from '{msg.topic}'")
    payload = str(msg.payload.decode())
    data.append((datetime.now(), payload))
    if len(data) > 100:
        data.pop(0)
        df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
        df["temperature"] = df["sensor_data"].apply(lambda x: eval(x)["temperature"])                                
        df["humidity"] = df["sensor_data"].apply(lambda x: eval(x)["humidity"]) 
        plt.clf() 
        plt.plot(df["timestamp"], df["temperature"], label="Temperature") 
        plt.plot(df["timestamp"], df["humidity"], label="Humidity") 
        plt.legend() 
        plt.draw() 
        plt.pause(0.1) 


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_start()
# Run for some time to receive messages
time.sleep(20)


client.loop_stop()  # Stop the loop
client.disconnect()  # Disconnect from the broker


plt.ion()
plt.figure()
plt.show()

# Run for some time to see the plot 
time.sleep(20)

plt.close()
