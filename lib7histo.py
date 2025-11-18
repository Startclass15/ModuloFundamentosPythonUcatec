import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(200)
y=np.random.randn(200)

#Metodo histogramas hist()
plt.hist(x,bins=20)
plt.hist(y, bins=20)
plt.show()