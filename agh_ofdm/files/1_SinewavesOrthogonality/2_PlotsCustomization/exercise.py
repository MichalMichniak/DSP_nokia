import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
plt.title("trianle + sinus")
plt.ylabel("amplitudo[a.u.]")
plt.xlabel("tempus[s]")
t = np.linspace(0,10,25)
plt.plot(t,3*signal.sawtooth(t,0.5)-np.sin(t),"--r",label = "sum")
plt.plot(t,3*signal.sawtooth(t,0.5),"-pg",label = "triangle")
plt.plot(t, -np.sin(t),"pb",label = "sinusoid")

plt.axhline(y=0,color = 'orange')
plt.xlim([0,10])
plt.ylim([-4,6])
plt.grid()

plt.legend()
plt.show()