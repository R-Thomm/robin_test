import numpy as np
import matplotlib.pyplot as plt
import time

t1 = time.time()

print("Hello")
print(np.sin(3.14))
time.sleep(5.2)
t2 = time.time()-t1

print(f'time without plots {t2}')

x = np.linspace(0,20,1000)
plt.plot(x,np.sin(x))
plt.show()

# plt.plot(np.cos(x),np.sin(x))
# plt.show()