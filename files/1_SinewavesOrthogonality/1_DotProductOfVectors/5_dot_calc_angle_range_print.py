import numpy as np
from mylib import rotate_vector
if __name__ == '__main__':
    green = np.array([0,1])
    blue = green.copy()
    for i in range(0,361,10):
        blue = rotate_vector(green,i)
        print(f"{i:03}:  {'' if np.dot(green,blue) < 0 else '+'}{np.dot(green,blue):.3f}")
        