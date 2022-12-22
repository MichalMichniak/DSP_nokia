import numpy as np
import matplotlib.pyplot as plt
from mylib.my_stem_plot import my_stem_plot

SAMPLE_NR = 10
SIN_FREQ = 3 

t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

samples =  np.sin(t*SIN_FREQ)
my_stem_plot(samples,f'samples, f_sig={SIN_FREQ}')

real = list()
for f in range(SAMPLE_NR):
    real.append(np.dot(np.cos(f*t),samples))

my_stem_plot(real,'my DFT real',y_range=(-6,7))

imag = list()
for f in range(SAMPLE_NR):
    imag.append(np.dot(-np.sin(f*t),samples))

my_stem_plot(imag,'my DFT imag',y_range=(-6,7))


