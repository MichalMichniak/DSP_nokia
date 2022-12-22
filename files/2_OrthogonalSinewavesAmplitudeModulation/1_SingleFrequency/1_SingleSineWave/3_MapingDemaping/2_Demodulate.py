import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# parameters
PERIOD_VECTOR_SIZE = 60
PERIOD_NUMBER = 5

# loading Rx vector from file and..
Rx = np.load('TxSignal_Exercise.npy')

# .. ploting it
plt.plot(Rx)
plt.grid()
plt.show()

# spliting vector into time slots coresponding to single periods
RxPeriods = np.reshape(Rx,(5,60))

# decoding amplitudes of Rx time slots

ampl_lst = [] # create amplitude list
for RxPeriod in RxPeriods:
    ampl = np.dot(np.sin(np.linspace(0, 2*pi,PERIOD_VECTOR_SIZE, endpoint=False)),
    RxPeriod)*2/PERIOD_VECTOR_SIZE # decode amplitude
    ampl_lst.append(ampl) # append amplitude to list
    
print(ampl_lst)  # print list
    



