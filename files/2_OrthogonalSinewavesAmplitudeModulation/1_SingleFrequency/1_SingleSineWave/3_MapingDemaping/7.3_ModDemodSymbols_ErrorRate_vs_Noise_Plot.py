import numpy as np
import matplotlib.pyplot as plt
from mapper_lib import symbol_to_ampl, ampl_to_symbol 

# PARAMETERS
TIME_VECTOR_SIZE = 60
TRANSMISIONS_NR = 1000

for sym_nr in [2,4,8]:
    err_number = []
    for deviation in np.linspace(0,5,20):
        t = np.linspace(0, 2*np.pi,TIME_VECTOR_SIZE, endpoint=False)
        Carrier = np.sin(t) 
        Ref     = Carrier
        # TRANSMISION-RECEPTION
        symbols_tx = np.random.randint(0,sym_nr,TRANSMISIONS_NR)    
        symbols_rx = list()
        for symbol in symbols_tx:        
            # modulation
            ampl = symbol_to_ampl(sym_nr,symbol)
            Tx = ampl*Carrier        
            # real channel
            Rx = Tx + np.random.normal(0.0,deviation,size = TIME_VECTOR_SIZE)   
            # demodulation
            ampl = (np.dot(Rx,Ref)/TIME_VECTOR_SIZE)*2  
            symbol = ampl_to_symbol(sym_nr,ampl)
            symbols_rx.append(symbol)
        # PRESENTATION   
        symbols_rx = np.array(symbols_rx) # list to numpy array
        err_number.append(sum(symbols_rx != symbols_tx))
    plt.plot(np.linspace(0,5,20),np.array(err_number),'p-',label=f"symbol nr = {sym_nr}")
plt.grid()
plt.xlabel("noise deviation")
plt.ylabel("error nr")
plt.legend()
plt.show()

