import serial
from datetime import datetime
import pandas as pd


def read_func(tekst):
    list_values = []
    list_in_floats = []

    list_values = []
    arduino = serial.Serial(port='COM6', baudrate=57600, timeout=1) # sprawdź na którym porcie masz swoje urządzenie

    # print('połączono')
    arduino_data = arduino.readline()
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')  # [data1]x[data2]x[data3]x[data4]



    for item in list_values:
        list_in_floats.append(float(item))

    now = datetime.now()
    act_time = now.strftime("%H:%M:%S")

    if tekst:
        print(f'{act_time} => odczyt : {list_in_floats}')
    else:
        # list_in_floats.append(now.hour)
        # list_in_floats.append(now.minute)
        # list_in_floats.append(now.second)
        return list_in_floats

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    

print(read_func(tekst=0))


