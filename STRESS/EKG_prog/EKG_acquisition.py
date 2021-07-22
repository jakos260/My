import serial_reading as sr
import prints
import pandas as pd

def main(df):
    
    def add_data():
        nonlocal signal_df
        nonlocal v_err
       
        try:
            data = pd.DataFrame([sr.read_func(tekst=0)], columns=df.columns)
            # print(data)
            signal_df = signal_df.append(data, ignore_index=True)
            prints.p(int(len(signal_df)*100/n))

        except ValueError:        
            v_err += 1 # licznik błędów

        return signal_df

    def stop():
        nonlocal one
        one = False

# _______________________main__________________________
    one = True
    signal_df = df
    v_err = 0 # liczba value errorów

    prints.question('ile próbek chcesz zebrać?')
    while True:    
        try:
            n =  int(input('podaj liczbę\n'))
            prints.message(f'pobieram {n} próbek')
            break
        except ValueError:
            prints.error('coś zepsułeś :( spróbuj jeszcze raz')


    while one:
        add_data()
        if len(signal_df) == n: stop()
    
    prints.message(f'Value error wystąpił {v_err} razy')
    return signal_df