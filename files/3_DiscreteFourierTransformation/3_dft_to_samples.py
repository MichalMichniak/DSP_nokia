import numpy as np
import matplotlib.pyplot as plt
SAMPLE_NR = 10
t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples = np.cos(2*t) + np.sin(4*t)/5

plt.title("orginal signal")
plt.stem(t,samples,"p-" )
plt.grid()
plt.show()