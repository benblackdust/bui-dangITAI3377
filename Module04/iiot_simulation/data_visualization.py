import paho.mqtt.client as mqtt 
import pandas as pd 
import matplotlib.pyplot as plt 
from datetime import datetime 

data = [] 


# Added to get additional information for troubleshooting the connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


def on_message(client, userdata, message): 
    print("Message received")
    payload = str(message.payload.decode())
    data.append((datetime.now(), payload)) 
    print("Checking Data size: ", len(data))
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
client.subscribe("sensor/data") 
client.loop_start() 

#plt.ion() 
#plt.figure() 
#plt.show()