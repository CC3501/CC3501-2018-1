import numpy as np

n = np.zeros((2, 2))
n[1][1] = np.nan

if np.isnan(n[1][1]):
    n[1][1] = -1
print n