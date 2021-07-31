import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import serial
from PIL import Image

def f(y1):
    if False:
        a = Image.open('a.PNG').convert('L')
        b = np.linalg.norm(a)
        norm = a/b
        z = norm*y1*100
    else:       
        z = np.zeros((11, 7))
        z[2,2:5] = 0.1
        z[3,2:5] = 0.1
        z[4,2:5] = 0.1
        z[5,2:5] = 0.1
        z[6,2:5] = 0.1
        z[7,2:6] = 0.1
        z[8,2:6] = 0.1
        z[9,3:6] = 0.1
        z[2:3,2:5] = y1
        z[1,3:4] = y1
    # print(z)
    return z

arduino = serial.Serial(port='COM3', baudrate=57600, timeout=1)
if arduino.is_open==True:
	print('\n_______________________________\n')
	print(arduino, "\n")

t0 = 0
fig = plt.figure()
im = plt.imshow(f(1), animated=True, interpolation='gaussian', cmap=plt.cm.jet, origin='lower', vmin=0, vmax=1)
fig.colorbar(im)

def animate(*args):
    global t0
    arduino_data = arduino.readline()      #ascii
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    values_list = decoded_values.split('x')  # [dane1]x[dane2]x[dane3]x[dane4]
    print(f'values_list {values_list}')
    
    y1 = 0 
    
    try:
        t = int(values_list[0]) - t0 
        y1 = int(values_list[1])/600  

    except ValueError:
        print('ValueError')
    
    im.set_array(f(y1))
    if t0 == 0:
        t0 =+ t
    plt.title(f'T = {t/1000} s')    

    arduino_data = 0
    values_list.clear()
    return im
    

ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()
arduino.close()