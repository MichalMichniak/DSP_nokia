import numpy as np
from mylib.my_stem_plot import my_stem_plot
from mylib.myDFT import myDFT


SAMPLE_NR = 10
t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)
samples = np.cos(t*1)*2/5 + np.sin(t*4)*4/5
my_stem_plot(samples,f'samples')

real,imag = myDFT(samples)
my_stem_plot(real, 'myDFT real')
my_stem_plot(imag, 'myDFT imag')

fft = np.fft.fft(samples)
my_stem_plot(fft.real, 'FFT real')
my_stem_plot(fft.imag, 'FFT imag')