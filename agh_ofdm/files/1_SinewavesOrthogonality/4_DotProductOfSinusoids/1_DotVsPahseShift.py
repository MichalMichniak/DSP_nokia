import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# PARAMETER
PHASE_SHIFT = pi/2 + pi/2

# VECTORS
t = np.linspace(0, 2*pi,30, endpoint=False)

Ref = np.sin(t)
Shifted = np.sin(t+PHASE_SHIFT)
Ref_mult_Shifted = Ref*Shifted
dot_product = np.sum(Ref_mult_Shifted) # use Ref_mult_Shifted

# PLOTS (HINT: use separate plots, not one with grid)

# components
fig,ax = plt.subplots(2)
fig.set_size_inches([5,7])
ax[0].plot(t,Ref,"bp-",label="Sin")
ax[0].plot(t,Shifted,"gp-",label="SinShift")
ax[0].grid()
ax[0].legend()
ax[0].axhline(0,-1,10,color="black")
ax[0].set_ylim([-1.1,1.1])
# multiplication, HINT: use "stem" function for ploting
ax[1].stem(t,Ref_mult_Shifted,markerfmt='C1o',label="Sin_Mul_SinShift")

ax[1].set_ylim([-1.1,1.1])
ax[1].grid()
ax[1].legend()

# print phase shift and dot product value
ax[1].text(-0.5, -1.7, f"dot_product = {dot_product:.2f}" , color="black")
ax[1].text(-0.5, -1.5, f"phase_shift = {PHASE_SHIFT:.2f}" , color="black")
plt.show()

