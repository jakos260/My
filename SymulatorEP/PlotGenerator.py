from itertools import count
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# df_v2 = pd.read_csv('claris/V2.Session 15 - Page 1.7.TXT', header=None)
# df_v3 = pd.read_csv('claris/V3.Session 15 - Page 1.7.TXT', header=None)
# df_v4 = pd.read_csv('claris/V4.Session 15 - Page 1.7.TXT', header=None)
# df_v5 = pd.read_csv('claris/V5.Session 15 - Page 1.7.TXT', header=None)
# df_v6 = pd.read_csv('claris/V6.Session 15 - Page 1.7.TXT', header=None)

fig = make_subplots(rows=6, cols=1, shared_xaxes=True, vertical_spacing=0.02)
fig2 = make_subplots(rows=6, cols=1)

# fig.update_layout(title_text="ECG")
fig2.update_layout(title_text="ECG")

for i in range(1, 7, 1):
    
    V = pd.read_csv(f'claris/V{i}.Session 15 - Page 1.{6+i}.TXT', header=None)
    V_x = np.linspace(0, len(V)/2000, len(V))
    V_y = np.array(V[0])    

    # fig.add_trace(go.Scatter(x=V_x, y=V_y, name=f'V{i}'), row=i, col=1)
    fig2.add_trace(go.Line(x=V_x, y=V_y, name=f'V{i}'), row=1, col=1)
    

HRA = pd.read_csv("claris/HRA.Session 15 - Page 3.7.TXT", header=None)
HRA_x = np.linspace(0, len(HRA)/2000, len(HRA))
HRA_y = np.array(HRA[0])
fig2.add_trace(go.Line(x=HRA_x, y=HRA_y, name=f'HRA'), row=2, col=1)

RVA = pd.read_csv("claris/RVA.Session 15 - Page 2.11.TXT", header=None)
RVA_x = np.linspace(0, len(RVA)/2000, len(RVA))
RVA_y = np.array(RVA[0])
fig2.add_trace(go.Line(x=RVA_x, y=RVA_y, name=f'RVA'), row=2, col=1)

for count, item in enumerate(["aVF", "aVL", "aVR"]):
    print(count, item)
    aVL = pd.read_csv(f"claris/{item}.Session 15 - Page 1.{6-count}.TXT", header=None)
    aVL_x = np.linspace(0, len(aVL)/2000, len(aVL))
    aVL_y = np.array(aVL[0])
    fig2.add_trace(go.Line(x=aVL_x, y=aVL_y, name=item), row=3, col=1)



for i in range(1, 4, 1):
    
    I = pd.read_csv(f'claris/{("I")*i}.Session 15 - Page 1.{i}.TXT', header=None)
    I_x = np.linspace(0, len(I)/2000, len(I))
    I_y = np.array(I[0])    

    # fig.add_trace(go.Scatter(x=V_x, y=V_y, name=f'V{i}'), row=i, col=1)
    fig2.add_trace(go.Line(x=I_x, y=I_y, name=f'{"I"*i}'), row=4, col=1)

HISd = pd.read_csv(f'claris/HIS d.Session 15 - Page 3.10.TXT', header=None)
HISd_x = np.linspace(0, len(HISd)/2000, len(HISd))
HISd_y = np.array(HISd[0])

HISm = pd.read_csv(f'claris/HIS m.Session 15 - Page 3.9.TXT', header=None)
HISm_x = np.linspace(0, len(HISm)/2000, len(HISm))
HISm_y = np.array(HISm[0]) 

HISp = pd.read_csv(f'claris/HIS p.Session 15 - Page 3.8.TXT', header=None)
HISp_x = np.linspace(0, len(HISp)/2000, len(HISp))
HISp_y = np.array(HISp[0]) 

fig2.add_trace(go.Line(x=HISd_x, y=HISd_y, name=f'HIS d'), row=5, col=1)
fig2.add_trace(go.Line(x=HISm_x, y=HISm_y, name=f'HIS m'), row=5, col=1)
fig2.add_trace(go.Line(x=HISp_x, y=HISp_y, name=f'HIS p'), row=5, col=1)

for i in range(4):
    
    CS = pd.read_csv(f'claris/CS {i*2+1}-{i*2+2}.Session 15 - Page 2.{10-i}.TXT', header=None)
    CS_x = np.linspace(0, len(CS)/2000, len(CS))
    CS_y = np.array(CS[0])    

    # fig.add_trace(go.Scatter(x=V_x, y=V_y, name=f'V{i}'), row=i, col=1)
    fig2.add_trace(go.Line(x=CS_x, y=CS_y, name=f'CS {i*2+1}-{i*2+2}'), row=6, col=1)

# fig.write_html('plot.html', auto_open=True)
fig2.write_html('plot2.html', auto_open=True)


# print
# fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)

# fig.add_trace(go.Scatter(x=x, y=y), row=1, col=1)

# fig.update_layout(height=1200, width=600,
#               title_text="Stacked Subplots with Shared X-Axes")
# fig['layout']['yaxis1'].update(domain=[0, 0.2])
# fig['layout']['yaxis2'].update(domain=[0.3, 0.7])
# fig['layout']['yaxis3'].update(domain=[0.8, 1])

# fig.write_html('plot.html', auto_open=True)
# fig = px.line(x=x, y=y)
# fig.show()