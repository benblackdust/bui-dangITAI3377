Lab 04 Conceptual Design of an IIoT Sensor Network & Protocol Experimentation


Group A
Members:
Hekim Aslan
Adam Blank
Benjamin Bui-dang
Orhan Gumus
Sumesh Surendran


This resides in a docker container configured with X support.  We were able to get MQTT functioning, the MQTT was installed into the Docker container with the command

RUN apt-get install -y mosquitto

Once installed a terminal session was launched inside the container and mosquitto was launched to listen for data.

The sensor simulation python script was used to generate random data and send it to the broker.  The console displayed the information received.

A data visualization script was created to read data from the broker.  This uses the MQTT client to read data in a separate thread.  This was able to be confirmed by printing the data to console.  Modificaitons to the provided code for the sensor were required as the client was being called before it was instantiated causing a runtime error. 

Attemping to open a MatPlotLib window to display a graph of the data was unsuccessful, and requires additional time an research to determine how to make this function.   Some changes were made to the code, moving the matplotlib update section out of the on_message function and creating the df dataframe as a global variable so that it can be accessed outisde the on_message function.  