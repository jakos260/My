
import serial
import time
import schedule
from datetime import datetime
import pandas as pd

def boat():
    import webbrowser
    url = 'https://www.youtube.com/watch?v=0qzLRlQFFQ4&ab_channel=VerbumDei'
    print('barka')
    webbrowser.open_new_tab(url)


def serial_read(tekst):
    list_values = []
    list_in_floats = []

    print('_____________________________')
    list_values = []
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

    # print('połączono z Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')  # dataxdataxdataxdata



    for item in list_values:
        list_in_floats.append(float(item))

    now = datetime.now()
    act_time = now.strftime("%H:%M:%S")

    if tekst:
        print(f'{act_time} => odczyt T : {list_in_floats}')
    else:
        list_in_floats.append(act_time)
        return list_in_floats

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()
    # print('no i elko')



print(serial_read(tekst=0))


