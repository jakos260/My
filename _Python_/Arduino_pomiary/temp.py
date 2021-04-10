
import serial
import time
import schedule
import datetime
import csv


def serial_read():
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

    # print('połączono z Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')  # dataxdataxdataxdata

    for item in list_values:
        list_in_floats.append(float(item))

    print(f'{datetime.datetime.now().time()} => odczyt T : {list_in_floats}')


    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    # print('no i elko')
    print('_____________________________')




# ----------------------------------------Main function------------------------------------

list_values = []
list_in_floats = []

print('      Lecimy z tym\nvvvvvvvvvvvvvvvvvvvvvv')

# Setting up the Arduino
schedule.every(5).seconds.do(serial_read)

while True:
    schedule.run_pending()
    time.sleep(1)

