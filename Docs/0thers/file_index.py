import numpy as np
import pandas as pd
import datetime
import os

def name():
    i = 1
    while os.path.exists(f'DF_{i}_{str(datetime.date.today())}.csv'):
        i += 1
    return f'DF_{i}_{str(datetime.date.today())}.csv'

def to_csv(df, overwrite):
    if overwrite:
        df.to_csv(f'DF_{str(datetime.date.today())}.csv')
    else:
        df.to_csv(name())

df = pd.DataFrame(np.random.randint(1, 99, (1, 4)))
to_csv(df, overwrite=True)