import numpy as np
import matplotlib.pyplot as plt

SAMPLE_NR = 10
FREQ = 3

def my_stem_plot(y,title,ax,y_range=None):
    x = np.arange(len(y))    
    ax.stem(x,y,'-p')

    ax.set_xticks(x)
    
    if y_range:
        ax.set_ylim(y_range)
        ax.set_yticks(np.arange(*y_range))
    
    ax.grid()
    ax.set_title(title)


fig,ax = plt.subplots(3,8, figsize=(20,5))
fig.tight_layout()
for n,i in enumerate([1, 4.0/5, 2.0/5, 1.0/5 ]):
    t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

    samples = i*np.cos(t*FREQ) #+ np.sin(t)

    my_stem_plot(samples,f'samples, cos_f={FREQ}', ax[0,n],y_range=(-6,7))

    fft = np.fft.fft(samples)
    my_stem_plot(np.real(fft),'real', ax[1,n], y_range=(-6,7))
    my_stem_plot(np.imag(fft),'imag', ax[2,n], y_range=(-6,7))

for idx,i in enumerate([1, 4.0/5, 2.0/5, 1.0/5 ]):
    n = idx+4
    t = np.linspace(0, 2*np.pi, SAMPLE_NR, endpoint=False)

    samples = i*np.sin(t*FREQ) #+ np.cos(t)

    my_stem_plot(samples,f'samples, sin_f={FREQ}', ax[0,n],y_range=(-6,7))

    fft = np.fft.fft(samples)
    my_stem_plot(np.real(fft),'real', ax[1,n], y_range=(-6,7))
    my_stem_plot(np.imag(fft),'imag', ax[2,n], y_range=(-6,7))

plt.show()
