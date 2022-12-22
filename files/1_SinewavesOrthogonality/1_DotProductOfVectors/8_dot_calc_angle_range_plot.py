from mylib import rotate_vector
import matplotlib.pyplot as plt
import numpy as np
v = [0, 1]

angle_list = []
dot_list = []

for angle in range(0,361,1):    
    angle_list.append(angle)    
    v_rot = rotate_vector(v,angle)
    dot = np.dot(v,v_rot)
    dot_list.append(dot)

plt.plot(angle_list,dot_list)

plt.xlabel("angle")
plt.ylabel("dot")

plt.grid()
plt.show()



