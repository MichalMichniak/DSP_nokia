import numpy as np

def myDFT(samples):
    t = np.linspace(0, 2*np.pi, len(samples), endpoint=False)
    imag = list()
    real = list()
    for f in range(len(samples)):
        imag.append(np.dot(-np.sin(f*t),samples))
        real.append(np.dot(np.cos(f*t),samples))
    return real,imag
    