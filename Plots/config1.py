'''
teoretyczne wartości U dla config1, W) CA3140E
'''
def U_out_generate (U_z, U_ref, R_g, R_fsr):
    U_out = U_ref*(1+(R_g/R_fsr))
    for i in range(len(U_out)):
        if U_out[i] > U_z:
            U_out[i] = U_z
    return U_out        


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

R_ref1 = 10e4 # Ohma
R_ref2 = 10e5 # Ohma
R_g1 = 2200 # Ohma
R_g2 = 10000 # Ohma
R_g3 = 100000 # Ohma

Uz = 10
U_ref = Uz*R_ref1/R_ref2
R_fsr = np.arange(0, 2*10e5, 1000)

# U_out = U_ref*(1+(R_g1/R_fsr))
# U_out2 = U_ref*(1+(R_g2/R_fsr))
# U_out3 = U_ref*(1+(R_g3/R_fsr))
U_out1 = U_out_generate(Uz, U_ref, R_g1, R_fsr)
U_out2 = U_out_generate(Uz, U_ref, R_g2, R_fsr)
U_out3 = U_out_generate(Uz, U_ref, R_g3, R_fsr)

plt.figure(figsize=(10,7))
plt.plot(R_fsr, U_out1, color = 'r', linestyle = '-', label = f'R_g = {R_g1/1000} kOhm')
plt.plot(R_fsr, U_out2, color = 'b', linestyle = '-', label = f'R_g = {R_g2/1000} kOhm')
plt.plot(R_fsr, U_out3, color = 'g', linestyle = '-', label = f'R_g = {R_g3/1000} kOhm')
plt.xlabel('R_fsr', fontsize = 12)
plt.ylabel('U_out', fontsize = 12)
# plt.xticks(np.arange(0, 50, step=5))
plt.legend()
plt.grid()
plt.show()