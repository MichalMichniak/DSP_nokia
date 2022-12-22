import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = (1.2, -3.4, 4.5, -1.2, 3.4)
NOISE_DEVIATION = 0.5
TANSMISION_NR = 100
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier = np.sin(t)
amplitudes_l = [] # create amplitude list
for i in range(TANSMISION_NR):
    amp = AMPL_VECTOR[i%4]
    Tx = amp*Carrier
    # channel
    Rx=Tx+np.random.normal(0.0,NOISE_DEVIATION,size = TIME_VECTOR_SIZE) 
    # demodulation
    ampl = np.dot(np.sin(np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)),
    Rx)*2/TIME_VECTOR_SIZE # decode amplitude
    amplitudes_l.append(ampl)

# PRESENTATION  


# Tx plot
plt.plot(np.array(amplitudes_l),"p",color = "royalblue")
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()




