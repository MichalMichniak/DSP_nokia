import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

SYMBOL_NR = 8
ampl = np.linspace(-1.5,1.5,1000)
symbol = list()
for amp in ampl:
    sym = ampl_to_symbol(SYMBOL_NR,amp)
    symbol.append(sym)

    
plt.plot(ampl,symbol,'p')    
    
plt.grid()
plt.title(f'Symbol nr: {SYMBOL_NR}')
plt.ylabel('Symbol')
plt.xlabel('Amplitude')
plt.show()


