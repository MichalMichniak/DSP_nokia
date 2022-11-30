import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

sampling = np.linspace(0,1,1000) * pi

t = np.linspace(0, 2*pi,30, endpoint=False)
lst = []
plt.axhline(0,-1,10,color="black")
for i in sampling:
    Ref = np.sin(t)
    Shifted = np.sin(t+i)
    lst.append(np.dot(Ref,Shifted))
plt.plot(sampling,np.array(lst),color="blue")
for i in [pi/8,pi/4,pi/3,pi/2,pi/2+pi/8,pi/2+pi/4,pi/2+pi/3,pi/2+pi/2,]:
    Ref = np.sin(t)
    Shifted = np.sin(t+i)
    plt.plot(i,np.dot(Ref,Shifted),"p",color="blue")

plt.xlabel("shift")
plt.ylabel("dot")
plt.grid()
plt.show()