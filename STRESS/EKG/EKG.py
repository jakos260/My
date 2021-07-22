from colorama.ansi import Style, Fore, Back
import serial
import time
import datetime
import schedule
import serial_reading as sr
# import signal2data as s2d
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def add_data():
    global signal_df
    global v_err

    try:
        data = pd.DataFrame([sr.read_func(tekst=0)], columns=col_names)
        signal_df = signal_df.append(data, ignore_index=True) # skomentuj żeby nie zapisywać
        # print(data)
        print('_____________________________')
        print(Fore.YELLOW + f'{int(len(signal_df)*100/n)} % ' + Style.RESET_ALL + 'colected...')

    except ValueError:        
        v_err += 1 # licznik błędów

    return signal_df

def signal2data():
    global l_err
    print('_____________________________')
    print('______przetwarzanie..._______\n')
    data_df = pd.DataFrame(columns=['ms', 'X'])
    for i in range(len(signal_df)-1):
        if signal_df['t'][i+1] - signal_df['t'][i] > T:
            l_err += (signal_df['t'][i+1] - signal_df['t'][i])/(T) -1 # zliczy ile próbek brakuje między [i] i [i+1] zapisem
            
    # t0 = min(signal_df['t'])
    t0 = signal_df['t'][0]
    data_df['ms'] = signal_df['t'] - t0
    data_df['X'] = signal_df['U']
    # data_df = data_df.set_index('ms')
        
    return data_df

def filename(extension, index):
    if index:
        i = 1
        while os.path.exists(f'data\EKG{i}_{str(datetime.date.today())}_E{int(l_err + v_err)}.{extension}'):
            i += 1
        return f'data\EKG{i}_{str(datetime.date.today())}_E{int(l_err + v_err)}.{extension}'
    else:
        return f'data\EKG_{str(datetime.date.today())}_E{int(l_err + v_err)}.{extension}' 

def to_excel():
    global signal_df
    data_df = signal2data()
    signal_df['value errors num'] = pd.DataFrame([v_err])
    signal_df['lost samples num'] = pd.DataFrame([l_err])

    writer = pd.ExcelWriter(filename('xlsx'))
    data_df.to_excel(writer, sheet_name='data')
    signal_df.to_excel(writer, sheet_name='signal')
    writer.save()
    print('__________data saved_________|', int(v_err), 'values errors |', int(l_err), 'lost samples |', len(signal_df),'samples collected |')

def to_csv():
    global signal_df
    global final_data
    final_data = signal2data()    
    
    print(Back.WHITE + Fore.BLACK + 'dodać index do zapisanej nazwy?' + Style.RESET_ALL)
    while True:
        x = input('y/n\n')
        if x == 'y':
            name = filename('csv', index=True)            
            final_data.to_csv(name)
            print(Fore.GREEN + f'zapisano plik pod nazwą <{name}>\n' + Style.RESET_ALL)
            break

        elif x == 'n':
            name = filename('csv', index=False)
            final_data.to_csv(name)
            print(Fore.BLUE + f'zapisano plik pod nazwą <{name}>\n' + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'coś zepsułeś :( spróbuj jeszcze raz\n' + Style.RESET_ALL)
    
    print(Fore.LIGHTBLUE_EX + f'__________data saved_________| {int(v_err)} values errors | {int(l_err)} lost samples | {len(signal_df)} samples collected |\n' + Style.RESET_ALL)
    

def plot():
    print(Back.WHITE + Fore.BLACK + 'chcesz może wykresik?' + Style.RESET_ALL)
    while True:
        x = input('y/n\n')
        if x == 'y':
            print(Fore.GREEN + 'rysuję Ci wykresik :)' + Style.RESET_ALL)
            print()
            x = final_data['ms']
            Y = final_data['X']
            plt.plot(x, Y, 'b', label='')
            plt.grid()
            plt.xlabel('ms')
            plt.ylabel('X')
            plt.show()
            break
        elif x == 'n':
            print(Fore.BLUE + 'może innym razem...' + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + 'coś zepsułeś :( spróbuj jeszcze raz' + Style.RESET_ALL)

def stop():
    # to_excel()
    to_csv()
    plot()
    global one
    one = False

# ___________________main__________________________
one = True
col_names = ['U', 't'] # podaj nazwy kolumn
signal_df = pd.DataFrame(columns=col_names)
v_err = 0 # liczba valuer errorów
l_err = 0 # liczba zgubionych danych
print(Fore.BLUE + '_________________________\n          heloł' + Style.RESET_ALL)
print(Back.WHITE + Fore.BLACK + 'ile próbek chcesz zebrać?' + Style.RESET_ALL)
while True:    
    try:
        n =  int(input('podaj liczbę\n'))
        print(Fore.BLUE + f'pobieram {n} próbek' + Style.RESET_ALL)
        break
    except ValueError:
        print(Fore.RED + 'coś zepsułeś :( spróbuj jeszcze raz' + Style.RESET_ALL)

# n = 50 # liczba próbek do zebrania
Fp = 100 # ustaw taką samą jak w mikrokontrolerze!
T = 1000/Fp

while one:
    add_data()
    if len(signal_df) == n: stop()
    

