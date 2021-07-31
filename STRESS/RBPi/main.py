from pandas.io.parquet import FastParquetImpl
import RPi.GPIO as GPIO
import Adafruit_ADS1x15 as adc
import time
import os
import pandas as pd


#____setup____
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
adc = adc.ADS1115()
GAIN = 1
'''
GAIN - wzmocnienie, zakres pomiarowy
2/3 = +/-6.144V
1 = +/-4.096V
2 = +/-2.048V
4 = +/-1.024V
8 = +/-0.512V
16 = +/-0.256V
'''
current_time = 0
last_time = 0
sampling_rate = 200 #[Hz]
T = 1/(sampling_rate * 1000)
channels_num = 1
# col_names = ['t', 'v1', 'v2', 'v3', 'v4']
col_names = ['t', 'v']
data = pd.DataFrame()
# values = [0, 0, 0 ,0 ,0]
# values = [0, 0]
values = [0]*(channels_num + 1)
values_list = [[]]

print('    |  T  |  1   |  2   |  3   |  4   |'.format(*range(4)))
print('_' * 42)

def data_save():
	for i in range(3):
		GPIO.output(16, 1)
		time.sleep(0.1)
		GPIO.output(16, 0)
		time.sleep(0.1)

	indeks = 1
	# file_name = f"/home/pi/data/record_{indeks}.csv"
	
	while (os.path.exists(f"/home/pi/data/record_{indeks}.csv")):
		indeks = indeks + 1
	# file_name = 

	data = pd.DataFrame(values_list, columns=col_names)
	data = data.drop(labels=0, axis=0)
	data.to_csv(f"/home/pi/data/record_{indeks}.csv", index=False)
	print('koniec') 

#____main loop____
begin_time = 0

while True:
	GPIO.output(16, 1)
	if (GPIO.input(20)): # ending process
		data_save()
		break
	
	current_time = time.perf_counter()
	if begin_time == 0:
		begin_time = current_time	
	
	if (current_time - last_time >= T):
		values[0] = round(current_time - begin_time, 3)
		for i in range(channels_num):
			values[i] = round(adc.read_adc(i, gain=GAIN) * (0.000125), 6) # 1.25E-6 dla gain = 1, UWAGA!
		print(f'|=> {values}')
		# print(pd.DataFrame(values)) # ['t': [values[0]], 'v1': [values[1]]]  
		# data.append(pd.DataFrame(values, columns=col_names), ignore_index = True)		
		last_time = current_time
		
		values_list.append(values)
		values = [0] * (channels_num + 1)
		