#code to take FFT of the dataset
#The first row of datafile cotains sampling frequency and second row contains no of samples


import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("testdata.txt")

f=data[0]
T=1/f
N=int(data[1])


data=data[1:N+1]


yf=np.fft.fft(data)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yf= 2.0/N * np.abs(yf[0:N/2])
np.savetxt("testdatafft.txt",yf)

plt.plot(xf,yf)
plt.grid()
plt.show()

