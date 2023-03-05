# modified code from https://youtu.be/Tnsm_JteSSE
#Python code for connecting Arduino to Python

import serial
import time
import schedule
import socket


def main_func():
    arduino = serial.Serial('COM7', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    s.send(decoded_values.encode()) # send values to webcam program
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))

    print(f'Collected readings from Arduino: {list_in_floats}')

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    print('Connection closed')
    print('<----------------------------->')


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []

# create a socket object
s = socket.socket()

# get the hostname of the receiver
host = 'localhost'

# define the port on which the receiver is listening
port = 12345

# connect to the receiver
s.connect((host, port))

print('Program started')

# Setting up the Arduino
#schedule.every(10).seconds.do(main_func)

while True:
    print('Calling main_func')
    main_func()
    time.sleep(10)

s.close() # close socket connection