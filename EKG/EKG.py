import serial
import time
import datetime
import schedule
import serial_read as sr
import pandas as pd
import numpy as np

def add_data():
    global signal_df
    global v_err

    try:
        data = pd.DataFrame([sr.read_func(tekst=0)], columns=col_names)
        signal_df = signal_df.append(data, ignore_index=True) # skomentuj żeby nie zapisywać
        # print(data)
        print('_____________________________')
        print(int(len(signal_df)*100/n), '% colected...')

    except ValueError:        
        v_err += 1 # licznik błędów

    return signal_df

def signal2data():
    global l_err
    print('_____________________________')
    print('______przetwarzanie..._______')
    data_df = pd.DataFrame(columns=['ms', 'mV'])
    for i in range(len(signal_df)-1):
        if signal_df['t'][i+1] - signal_df['t'][i] > T:
            l_err += (signal_df['t'][i+1] - signal_df['t'][i])/T # zliczy ile próbek brakuje między ostatnim i przedostatnim zapisem

    # t0 = min(signal_df['t'])
    t0 = signal_df['t'][0]
    data_df['ms'] = signal_df['t'] - t0
    data_df['mV'] = signal_df['U'] * 0.444326 - 300
    data_df = data_df.set_index('ms')
        
    return data_df


def to_excel():
    name = 'data\EKG_' + str(datetime.date.today()) + '.xlsx'
    global signal_df
    data_df = signal2data()
    signal_df['value errors num'] = pd.DataFrame([v_err])
    signal_df['lost samples num'] = pd.DataFrame([l_err])

    writer = pd.ExcelWriter(name)
    data_df.to_excel(writer, sheet_name='data')
    signal_df.to_excel(writer, sheet_name='signal')
    writer.save()
    print('__________data saved_________|', int(v_err), 'values errors |', int(l_err), 'lost samples |', len(signal_df),'samples collected |')

def stop():
    to_excel()
    global one
    one = False

# ___________________main__________________________
one = True
col_names = ['U', 't'] # podaj nazwy kolumn
signal_df = pd.DataFrame(columns=col_names)
v_err = 0 # liczba valuer errorów
l_err = 0 # liczba zgubionych danych
n = 200 # liczba próbek do zebrania
Fp = 100 # ustaw taką samą jak w mikrokontrolerze!
T = 1000/Fp

while one:
    add_data()
    if len(signal_df) == n: stop()
    

