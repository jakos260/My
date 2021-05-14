import numpy as np
import matplotlib.pyplot as plt
'''
_______________________________________________
                NIE DZIAŁAM XD
_______________________________________________
x = np.arange(12) + 7
y = np.array([304.08994, 229.13878, 173.71886, 135.75499,
               111.096794, 94.25109, 81.55578, 71.30187, 
               62.146603, 54.212032, 49.20715, 46.765743])
y_t = y

plt.figure(figsize=(10,7))
plt.plot(x, y, 'r.', label='data')
plt.legend()
plt.show()

#fit the model
fit = np.polyfit(x, np.log(y_t), 1)

#view the output of the model
print(f'y=ab^x\na = {fit[1]} | b = {fit[0]}')

y_pred = fit[1]*fit[0]**x


plt.figure(figsize=(10,7))
plt.plot(x, y, 'r.', label='data')
plt.plot(x, y_pred, 'b', label='fit')
plt.grid()
plt.legend()
plt.show()
'''