import pandas as pd
import prints


def main(df):

    def set_time():       
        nonlocal l_err
        nonlocal data        

        for i in range(len(df)-1):
            if df['t'][i+1] - df['t'][i] > T:
                l_err += (df['t'][i+1] - df['t'][i])/T - 1
                # zliczy ile próbek brakuje między [i] i [i+1] zapisem
            
        if l_err > 0:
            prints.message(f'utracono łącznie {int(l_err)} próbek')

        t0 = df['t'][0]
        data['t'] = df['t'] - t0
        data['V'] = df['V']
        '''
        tu można zrobić funkcję przewarzania bitów na napięcie, tylko czy jest sens?
        '''
        # data_df = data_df.set_index('ms')
        

# _______________________main__________________________

    prints.message('przetwarzanie...')
    Fp = 100 # ustaw taką samą jak w mikrokontrolerze!
    T = 1000/Fp

    data = pd.DataFrame(columns=df.columns)

    l_err = 0
    set_time()

    '''
    _________________________________________________
    tutaj będzie całe filtrowanie i inne takie rzeczy
    _________________________________________________
    '''
    return data