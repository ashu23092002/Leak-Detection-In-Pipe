import os
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

# Reading excel files from current directory
directory_path = os.path.dirname(os.path.abspath(__file__))

file_list = os.listdir(directory_path)

excel_file_list = [file for file in file_list if file.endswith('.csv')]

excel_file_keys = []

for excel_file in excel_file_list:
    first_index = excel_file.find('_')
    second_index = excel_file.find('_', first_index + 1)

    excel_file_keys.append(excel_file[first_index + 1 : second_index])
# print(excel_file_keys)

excel_file_data = []

for excel_file in excel_file_list:
    file_path = os.path.join(directory_path, excel_file)
    # print(file_path)
    data_values = pd.read_csv(file_path)
    excel_file_data.append(data_values.iloc[:,1].values)

min_samples = len(excel_file_data[0])
for file in excel_file_data:
    min_samples = min(len(file), min_samples)

excel_file_data = [file[:min_samples] for file in excel_file_data]

# Storing excel file sample data and using excel file name as key for dictionary
leak_samples = dict(zip(excel_file_keys, excel_file_data))

file_path = os.path.join(directory_path, excel_file_list[0])
data = pd.read_csv(file_path)
time_samples = data.iloc[:,0].values
time_samples = time_samples[:min_samples]

pprint.pprint(leak_samples)

# FFT analsis of samples 
fft_analysed_samples = dict()
for key, value in leak_samples.items():
    fft_analysed_samples[key] = fft(value)

# Creating frequency axis sampling points
N = min_samples
n = np.arange(N)

sampling_interval = time_samples[1]
T = N * sampling_interval

freq = n / T
freq_max_limit = np.median(freq)

N = 100000
n = np.arange(N)

sampling_interval = time_samples[1]
T = N * sampling_interval

freq1 = n / T
freq1_max_limit = np.median(freq1)

x = leak_samples[excel_file_keys[1]]
x = x[0:N]
X = fft(x)

print(len(fft_analysed_samples[excel_file_keys[0]]))
print(1/sampling_interval)

plt.plot(freq1, abs(X), color = 'blue', alpha = 0.5)
# plt.plot(freq, abs(fft_analysed_samples[excel_file_keys[0]]), color = 'red', alpha = 0.5)
plt.xlim([-100, freq_max_limit])
plt.show()