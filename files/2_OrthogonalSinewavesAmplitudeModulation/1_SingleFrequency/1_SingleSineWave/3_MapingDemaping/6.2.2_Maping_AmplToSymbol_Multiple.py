import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import ampl_to_symbol

ampl = np.linspace(-1.5,1.5,1000)

for symbol_nr in 2,4,8:
    symbol = list()
    for amp in ampl:
        sym = ampl_to_symbol(symbol_nr,amp)
        symbol.append(sym)  
    plt.plot(ampl,symbol,'p-', label=f"symbol nr = {symbol_nr}")    
    
plt.legend()    
plt.grid()
plt.xlabel('Symbol')
plt.ylabel('Amplitude')
plt.show()
