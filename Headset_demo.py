from nanpy import (ArduinoApi, SerialManager,Servo)
import urllib.request

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")

counter = 0
servo = Servo(3)
link = "http://192.168.1.85:1337/"
f = urllib.request.urlopen(link)
servo.write(0)

while(True):
    f = urllib.request.urlopen(link)
    myfile = f.read()
    full_rot_bool = True
    
    if (full_rot_bool):
        servo.write(180)
        full_rot_bool = False

    else:
        servo.write(0)
        full_rot_bool = True
