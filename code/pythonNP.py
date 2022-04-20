import numpy as np
import psutil
# Getting % usage of virtual_memory ( 3rd field)

r = np.random.rand(10000,10000)

np.matmul(r,r)
print('RAM memory % used:', psutil.virtual_memory()[2])
