import serial
import time
import schedule
import serial_read as sr
import pandas as pd

def add_data():
    global df
    global miss_value

    try:        
        data = pd.DataFrame([sr.read_func(tekst=0)], columns=['T','L','H','M','S'])
        df = df.append(data, ignore_index=True) # skomentuj żeby nie ładować do pamieci
        print(data)

    except ValueError:
        miss_value += 1

    return df


def to_excel():
    df.to_excel('data/temp.xlsx', sheet_name='Dane')
    print('________data saved_________|', miss_value, 'missing values |', len(df),'samples |')

def stop():
    to_excel()
    global one
    one = False


# ___________________main__________________________

one = True
df = pd.DataFrame(columns=['T','L','H','M','S'])
miss_value = 0

      
schedule.every(1).seconds.do(add_data)    
schedule.every(5).seconds.do(to_excel) # skomentuj żeby nie ładować do pamieci
# schedule.every().day.at('00:24').do(stop)
# schedule.every().day.at('21:37').do(sr.boat)


while one:
    schedule.run_pending()
    if len(df) == 50: stop() # stop jeśli zebrano n danyc
    # time.sleep(1)
    

