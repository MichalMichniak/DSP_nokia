import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# loading Rx vector from file and..
Rx = np.load('TxSignal.npy')

# .. ploting it
plt.plot(Rx)
plt.axhline(y=0,color='black')
plt.grid()
plt.show()

# PARAMETERS
TIME_VECTOR_SIZE = 60
CARRIER_NR = 6

# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

ampl_l = []
for i in range(1,CARRIER_NR+1):
    f = np.sin(i*t)
    dot  = np.dot(f, Rx) 
    ampl = dot * 2/TIME_VECTOR_SIZE
    ampl_l.append(ampl) 

# PRESENTATION
for a in ampl_l:
    print(f'{a:0.2f}',end=', ')
    
    