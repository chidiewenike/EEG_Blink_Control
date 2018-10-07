# EEG_Blink_Control
Allows for the control of specific devices using blinks with the Neurosky MindWave. When connecting to the GPIOs of a Raspberry Pi, 
the user can control LEDs, motors, sensors, and more. The current Headset_demo allows for the complete rotation of a servo motor.

# server.js
This JavaScript program reads blink data transmitted to the dongle from the Neurosky MindWave headset. The data is then transmitted to a localhost to be accessed by the Raspberry Pi.

# Headset_demo.py
This program is intended to be run on the Raspberry Pi. The RPi accesses the localhost and waits until it retrieves the blink data. When it is retrieved, it will then rotate the servo motor either 180 degrees or -180 degrees. The code can be easily adjusted to control any circuit module.  
