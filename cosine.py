import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0,15,0.1)
b=np.sin(a)
c=np.cos(a)
plt.plot(a,b,a,c)
plt.xlabel('Values from 0 to 15')
plt.ylabel('Plot of sin and cos')
plt.legend(['sin(a)','cos(b)'])
plt.show()

