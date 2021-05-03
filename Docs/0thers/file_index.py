import numpy as np
import pandas as pd
import datetime

def name()
    name = 'data\DF_' + str(datetime.date.today())
    return 

def to_csv(df, overwrite):
    if overwrite:
        df.to_csv(name())
    else:
        df.to_csv(name())

df = np.random.random((2, 5))
to_csv(df, overwrite=True)