import keyboard 
import paho.mqtt.client as mqtt
import time


client = mqtt.Client()
client.connect('localhost', 1884)

while True: 
	if keyboard.is_pressed('w'):
		client.publish("robot/control", 'Forward')
	elif keyboard.is_pressed('a'):
		client.publish("robot/control", 'Left')
	elif keyboard.is_pressed('d'):
		client.publish("robot/control", 'Right')
	elif keyboard.is_pressed('s'):
		client.publish("robot/control", 'Stop')

	time.sleep(0.001)

