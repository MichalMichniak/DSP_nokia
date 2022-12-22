import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETERS
TIME_VECTOR_SIZE = 60
AMPL_VECTOR = np.linspace(1,4,8)#(1, 2, 3, 4)
NOISE_DEVIATION = 0.4
TANSMISION_NR = 100
# CALCULATION
t = np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)

Carrier = np.sin(t)
amplitudes_l = [] # create amplitude list
for i in range(TANSMISION_NR):
    amp = AMPL_VECTOR[i%len(AMPL_VECTOR)]
    Tx = amp*Carrier
    # channel
    Rx=Tx+np.random.normal(0.0,NOISE_DEVIATION,size = TIME_VECTOR_SIZE) 
    # demodulation
    ampl = np.dot(np.sin(np.linspace(0, 2*pi,TIME_VECTOR_SIZE, endpoint=False)),
    Rx)*2/TIME_VECTOR_SIZE # decode amplitude
    amplitudes_l.append(ampl)

# PRESENTATION  


# Tx plot
plt.title(f"NOISE_DEVIATION = {NOISE_DEVIATION}")
plt.plot(np.array(amplitudes_l)[0::4],"p",color = "red")
plt.plot(np.array(amplitudes_l)[1::4],"p",color = "orange")
plt.plot(np.array(amplitudes_l)[2::4],"p",color = "green")
plt.plot(np.array(amplitudes_l)[3::4],"p",color = "blue")
plt.plot(np.array(amplitudes_l)[4::4],"p",color = "red")
plt.plot(np.array(amplitudes_l)[5::4],"p",color = "orange")
plt.plot(np.array(amplitudes_l)[6::4],"p",color = "green")
plt.plot(np.array(amplitudes_l)[7::4],"p",color = "blue")
plt.axhline(y=0,color='black')
plt.grid(axis='y')
plt.show()




