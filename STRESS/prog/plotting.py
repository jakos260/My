import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random
import serial
from serial.serialutil import Timeout


arduino = serial.Serial(port='COM3', baudrate=57600, timeout=1)

if arduino.is_open==True:
	print('\n_______________________________\n')
	print(arduino, "\n")

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    
    #Aquire and parse data from serial port
    arduino_data = arduino.readline()      #ascii
    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    values_list = decoded_values.split('x')  # [data1]x[data2]x[data3]x[data4]
    # print(f'values_list {values_list}')
    
    
    try:
        t = int(values_list[0])
        y = int(values_list[1])   

    except ValueError:
        print('ValueError')
    
    	
	# Add x and y to lists
    xs.append(t)
    ys.append(y)
    
    T = 40
    if len(xs) > T:
        xs = xs[-T:]
        ys = ys[-T:]
    

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, 'b')


    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)
    plt.ylabel('Y')
    plt.grid()
    plt.axis([xs[0], xs[0]+T*10, 0, 1100])

    arduino_data = 0
    values_list.clear()
    

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
plt.show()
arduino.close()