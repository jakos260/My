import serial
import time
import schedule
import serial_read as sr
import pandas as pd

def add_data():
    global df
    global miss_value

    try:        
        data = pd.DataFrame([sr.read_func(tekst=0)], columns=['T', 'L', 'H'])
        df = df.append(data, ignore_index=True)
        # print(df, type(df), df.shape)
        # print(data, type(data), data.shape)
        print(data)

    except ValueError:
        miss_value += 1

    return df


def to_excel():
    df.to_excel('data/temp.xlsx', sheet_name='Dane')
    print('________data saved_________|', miss_value, 'missing values |')

def stop():
    to_excel()
    global one
    one = False


# ___________________main__________________________

one = True
df = pd.DataFrame(columns=['T','L','H'])
miss_value = 0

      
schedule.every(20).seconds.do(add_data)    
schedule.every(100).seconds.do(to_excel)
schedule.every().day.at('19:55').do(stop)
# schedule.every().day.at('21:37').do(sr.boat)


while one:
    schedule.run_pending()
    # time.sleep(1)
    

