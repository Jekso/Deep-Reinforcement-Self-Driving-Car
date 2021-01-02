import paho.mqtt.client as mqtt
from gpiozero import Robot


client = mqtt.Client()
client.connect('192.168.1.105', 1884)


robot = Robot((23, 24), (27, 17))


def on_connect(client, userdata, flags, rc):
    client.subscribe("robot/control")

def on_message(client, userdata, message):
    command = message.payload.decode()
    if command == 'Forward':
    	robot.forward()
    elif command == 'Stop':
    	robot.stop()
    elif command == 'Left':
    	robot.left()
    if command == 'Right':
    	robot.right()

while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()