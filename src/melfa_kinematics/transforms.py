import numpy as np

def Trans(x, y, z):
    T = np.array([
       [1, 0, 0, x],
       [0, 1, 0, y],
       [0, 0, 1, z],
       [0, 0, 0, 1]
    ])


    return T

