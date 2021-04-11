import serial
import time
import schedule
import serial_read as sr
import pandas as pd

def add_data():
    global df
    data = pd.DataFrame([sr.serial_read(tekst=0)], columns=['T', 'L', 'H'])
    df = df.append(data, ignore_index=True)
    # print(df, type(df), df.shape)
    # print(data, type(data), data.shape)
    print(data)
    return df


def to_excel():
    df.to_excel('temp.xlsx', sheet_name='Dane')
    print('________data saved_________')

def stop():
    to_excel()
    global one
    one = False


# ___________________main__________________________

one = True
df = pd.DataFrame(columns=['T','L','H'])

schedule.every(1).seconds.do(add_data)
schedule.every(5).seconds.do(to_excel)
schedule.every().day.at('09:49').do(stop)
schedule.every().day.at('21:37').do(sr.boat)


while one:
    schedule.run_pending()
    time.sleep(1)

