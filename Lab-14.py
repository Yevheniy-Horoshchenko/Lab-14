import matplotlib.pyplot as plt
import numpy as np
xi = [1.7,1.9,2.1,2.3,2.5,2.7]
yi = [2.7,3.1706,3.6571,4.1562,4.6653,5.1824]
x = np.linspace(1,4,30)
plt.plot(xi,yi,'g')
plt.title("LB_14_Eiler")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
