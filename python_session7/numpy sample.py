import numpy as np
import time

array =np.randrom.rand(10000, 10000)
x=array+array.T
start = time.time()
x.sum()
end = time.time()-start
print