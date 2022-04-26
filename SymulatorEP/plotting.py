import os
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

dataPath = "sygnay"
dataFrames = os.listdir(dataPath)

fig2 = make_subplots(rows=3, cols=1)
fig2.update_layout(title_text="ECG")
i = 0
for df in dataFrames:
    name = os.path.splitext(df)[0].split("-")
    
    V = pd.read_csv(os.path.join(dataPath, df), header=None)
    V_y = np.concatenate((np.zeros(len(V[0])), np.array(V[0]), np.zeros(len(V[0])*8)), axis=None)
    V_x = np.linspace(0, len(V_y)/2000, len(V_y))
    if(name[0] == 'I' and name[-1] == 'v2'):
        fig2.add_trace(go.Line(x=V_x, y=V_y, name=df), row=1, col=1)
    if(name[0] == 'II' and name[-1] == 'v2'):
        fig2.add_trace(go.Line(x=V_x, y=V_y, name=df), row=2, col=1)
    if(name[0] == 'VI' and name[-1] == 'v2'):
        fig2.add_trace(go.Line(x=V_x, y=V_y, name=df), row=3, col=1)
    # if(name[0] == 'I' and name[-1] == 'v2'):
    #     fig2.add_trace(go.Line(x=V_x, y=V_y, name=df), row=1, col=1)



# fig2.write_html('ECGsygnay.html', auto_open=True)
fig2.show()